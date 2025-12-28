# Quick Start - Docker Deployment

## Run on Windows (Your Current System)

### 1. Install Docker Desktop
Download and install: https://docs.docker.com/desktop/install/windows-install/

### 2. Deploy MagicMirror
```cmd
# Open PowerShell or Command Prompt in your project folder
cd D:\test\face_recogonation

# Run deployment script
deploy-docker.bat
```

### 3. Access Your MagicMirror
```
🌐 MagicMirror: http://localhost:8080
📹 Face API: http://localhost:5000
```

**That's it!** Docker Desktop handles everything on Windows.

---

## Run on Linux

### Files to Copy to Linux

Copy these files/folders from Windows to your Linux machine:

```
📁 Your Project Folder
├── 📄 Dockerfile
├── 📄 docker-compose.yml
├── 📄 .dockerignore
├── 📄 deploy-docker.sh
├── 📁 face_recognition/
│   ├── main.py
│   ├── train_faces.py
│   ├── encodings.pickle
│   └── dataset/
│       └── YourName/ (your face photos)
└── 📁 MagicMirror/
    ├── config/
    │   └── config.js
    └── modules/
        └── MMM-VoiceAssistant/
            ├── voice_assistant.py
            ├── node_helper.js
            ├── MMM-VoiceAssistant.js
            └── MMM-VoiceAssistant.css
```

## Transfer Methods

### Option 1: USB Drive
```bash
# On Windows - Copy to USB
# Copy entire project folder to USB drive

# On Linux - Copy from USB
cp -r /media/usb/face_recogonation ~/magicmirror-project
cd ~/magicmirror-project
```

### Option 2: SCP (Network Transfer)
```bash
# On Windows (PowerShell or Git Bash)
scp -r D:\test\face_recogonation user@linux-ip:~/magicmirror-project

# On Linux
cd ~/magicmirror-project
```

### Option 3: Git (Recommended)
```bash
# On Windows - Push to Git
git init
git add .
git commit -m "Initial commit"
git push origin main

# On Linux - Clone
git clone <your-repo-url> ~/magicmirror-project
cd ~/magicmirror-project
```

## Run on Linux

### 1. Install Docker (One-time)
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, then verify
docker --version
```

### 2. Deploy MagicMirror
```bash
cd ~/magicmirror-project

# Make script executable
chmod +x deploy-docker.sh

# Run deployment
./deploy-docker.sh
```

### 3. Access Your MagicMirror
```
🌐 MagicMirror: http://localhost:8080
📹 Face API: http://localhost:5000
```

## That's It!

Your MagicMirror Voice Assistant is now running in Docker with:
- ✅ Face recognition
- ✅ Voice commands
- ✅ All features working
- ✅ Zero manual installation

## Useful Commands

```bash
# View logs
docker-compose logs -f

# Stop
docker-compose stop

# Start again
docker-compose start

# Restart
docker-compose restart

# Remove everything
docker-compose down
```

## Minimum Files Needed

If you want minimal setup, copy only:
1. `Dockerfile`
2. `docker-compose.yml`
3. `deploy-docker.sh`
4. `face_recognition/` folder
5. `MagicMirror/modules/MMM-VoiceAssistant/` folder
6. `MagicMirror/config/config.js`

Docker will handle the rest!
