import os
import subprocess
import sys
import urllib.request

# URL for dlib 19.22.99 for Python 3.10 on Windows x64
DLIB_URL = "https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/main/dlib-19.22.99-cp310-cp310-win_amd64.whl"
WHEEL_NAME = "dlib-19.22.99-cp310-cp310-win_amd64.whl"

def install_dlib():
    print(f"Downloading {WHEEL_NAME}...")
    try:
        urllib.request.urlretrieve(DLIB_URL, WHEEL_NAME)
        print("Download complete.")
    except Exception as e:
        print(f"Failed to download dlib wheel: {e}")
        return

    print("Installing dlib...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", WHEEL_NAME])
        print("Successfully installed dlib!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dlib: {e}")
    finally:
        # Cleanup
        if os.path.exists(WHEEL_NAME):
            os.remove(WHEEL_NAME)

if __name__ == "__main__":
    install_dlib()
