import cv2
import os
import time

KNOWN_FACES_DIR = "known_faces"

def capture_face():
    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)
        
    name = input("Enter the name of the person: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty.")
        return

    # Create a directory for this person
    person_dir = os.path.join(KNOWN_FACES_DIR, name)
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
        print(f"[INFO] Created directory: {person_dir}")
    else:
        print(f"[INFO] Adding to existing directory: {person_dir}")

    print(f"[INFO] Opening webcam for {name}...")
    print("[INSTRUCTIONS] Press 'c' to capture a photo, 'q' to quit.")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return

    count = len(os.listdir(person_dir)) # Start count based on existing files

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to capture frame.")
            break

        cv2.imshow(f"Capture Face: {name} - Press 'c' to Capture, 'q' to Quit", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            filename = f"{name}_{count:04d}.jpg"
            filepath = os.path.join(person_dir, filename)
            cv2.imwrite(filepath, frame)
            count += 1
            print(f"[SUCCESS] Saved image #{count}: {filepath}")
        elif key == ord('q'):
            print(f"[INFO] Finished capturing. Total images in folder: {count}")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_face()
