import face_recognition
import pickle
import os
import cv2

# Directory containing images of known faces
KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "encodings.pickle"

def train_faces():
    known_encodings = []
    known_names = []

    print(f"[INFO] Scanning directory: {KNOWN_FACES_DIR}...")
    
    if not os.path.exists(KNOWN_FACES_DIR):
        print(f"[ERROR] Directory '{KNOWN_FACES_DIR}' not found. Please create it and add images.")
        return

    # List to hold all image paths and their corresponding names
    images_to_process = []

    # Walk through the directory to find files
    for root, dirs, files in os.walk(KNOWN_FACES_DIR):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Determine name: if in a subdirectory, use subdir name; else use filename
                if root == KNOWN_FACES_DIR:
                    # File is directly in KNOWN_FACES_DIR (old style)
                    name = os.path.splitext(filename)[0]
                else:
                    # File is in a subdirectory (new style: known_faces/Name/img.jpg)
                    name = os.path.basename(root)
                
                image_path = os.path.join(root, filename)
                images_to_process.append((name, image_path))

    if not images_to_process:
        print("[INFO] No images found. Please add images of faces.")
        return

    print(f"[INFO] Found {len(images_to_process)} images to process.")

    for name, image_path in images_to_process:
        print(f"[INFO] Processing {name} ({os.path.basename(image_path)})...")
        
        image = cv2.imread(image_path)
        if image is None:
            print(f"[WARNING] Could not read image: {image_path}")
            continue

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect the face locations
        boxes = face_recognition.face_locations(rgb_image, model="hog")

        # Compute the facial embedding
        encodings = face_recognition.face_encodings(rgb_image, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(name)

    print(f"[INFO] Serializing {len(known_encodings)} encodings...")
    data = {"encodings": known_encodings, "names": known_names}
    
    with open(ENCODINGS_FILE, "wb") as f:
        f.write(pickle.dumps(data))
        
    print(f"[INFO] Encodings saved to {ENCODINGS_FILE}")

if __name__ == "__main__":
    train_faces()
