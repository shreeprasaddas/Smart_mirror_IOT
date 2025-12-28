import face_recognition
import cv2
import pickle
import sys
import pyttsx3
import time
import os
import random
import requests
import threading
from flask import Flask, Response, jsonify
from flask_cors import CORS

ENCODINGS_FILE = "encodings.pickle"

# Flask and Global vars
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
output_frame = None
lock = threading.Lock()

# Greeting state
current_greeting_data = {"name": "", "greeting": "", "timestamp": 0}
greeting_lock = threading.Lock()

# Initialize TTS globally, but use carefully
engine = None 

def speak(text):
    # Re-initialize engine inside thread if needed, or just use a simple print for now if TTS acts up
    # pyttsx3 can be tricky with threads. We'll try initializing it locally.
    try:
        local_engine = pyttsx3.init()
        print(f"[SAYING] {text}")
        local_engine.say(text)
        local_engine.runAndWait()
    except Exception as e:
        print(f"[TTS ERROR] {e}")

def detect_faces():
    global output_frame, lock

    if not os.path.exists(ENCODINGS_FILE):
        print(f"[ERROR] {ENCODINGS_FILE} not found. Please run train_faces.py first.")
        return

    print("[INFO] Loading encodings...")
    data = pickle.loads(open(ENCODINGS_FILE, "rb").read())
    
    print("[INFO] Starting video stream...")
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("[ERROR] Could not access webcam.")
        return

    # Track greeted names to avoid repetitive greetings
    greeted_names = {}
    GREETING_COOLDOWN = 15 

    while True:
        ret, frame = video_capture.read()
        if not ret:
            continue

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color to RGB color
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # tolerance=0.45 is stricter
            matches = face_recognition.compare_faces(data["encodings"], face_encoding, tolerance=0.45)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = data["names"][first_match_index]
            
            face_names.append(name)
            
            # GREETING LOGIC
            if name != "Unknown":
                current_time = time.time()
                last_greeted = greeted_names.get(name, 0)
                
                # Only update greeting data if cooldown has expired (NEW detection)
                if current_time - last_greeted > GREETING_COOLDOWN:
                    greeted_names[name] = current_time  # Mark as greeted
                    
                    greetings = [
                        f"Hello, {name}",
                        f"Welcome back, {name}",
                        f"Good to see you, {name}",
                        f"Hi there, {name}",
                        f"Greetings, {name}",
                        f"Hey {name}, hope you are doing well"
                    ]
                    greeting = random.choice(greetings)
                    
                    # Update greeting data for MagicMirror (ONLY on new detection)
                    with greeting_lock:
                        current_greeting_data["name"] = name
                        current_greeting_data["greeting"] = greeting
                        current_greeting_data["timestamp"] = current_time
                    
                    # Log to console instead of speaking
                    print(f"[DETECTED] {name} - Notification sent")
                    
                    # Send notification to MagicMirror
                   
        # Clear greeting if no faces detected
        if len(face_names) == 0 or all(name == "Unknown" for name in face_names):
            with greeting_lock:
                current_greeting_data["name"] = ""
                current_greeting_data["greeting"] = ""
                current_greeting_data["timestamp"] = 0

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)

        # Acquire lock and copy frame for Flask
        with lock:
            output_frame = frame.copy()

    video_capture.release()

def generate():
    # Video streaming generator function
    global output_frame, lock
    while True:
        with lock:
            if output_frame is None:
                continue
            (flag, encodedImage) = cv2.imencode(".jpg", output_frame)
            if not flag:
                continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
              bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/current_greeting")
def current_greeting():
    with greeting_lock:
        return jsonify(current_greeting_data)

if __name__ == "__main__":
    # Start detection in a background thread
    t = threading.Thread(target=detect_faces)
    t.daemon = True
    t.start()
    
    # Start Flask app
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True, use_reloader=False)
