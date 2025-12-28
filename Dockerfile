# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Node.js dependencies
    curl \
    git \
    # Python dependencies
    python3 \
    python3-pip \
    python3-dev \
    # Face recognition dependencies
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-all-dev \
    # Audio dependencies
    portaudio19-dev \
    python3-pyaudio \
    espeak \
    libespeak-dev \
    flac \
    alsa-utils \
    # Video dependencies
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    # Cleanup
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 18.x
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Set working directory
WORKDIR /app

# Install Python packages
RUN pip3 install --no-cache-dir \
    face_recognition \
    opencv-python-headless \
    SpeechRecognition \
    pyttsx3 \
    requests \
    Flask \
    Flask-CORS \
    pyaudio

# Clone MagicMirror
RUN git clone https://github.com/MagicMirrorOrg/MagicMirror.git /app/MagicMirror

# Install MagicMirror dependencies
WORKDIR /app/MagicMirror
RUN npm install --only=prod --omit=dev

# Copy project files
COPY ./face_recognition /app/face_recognition
COPY ./MagicMirror/modules/MMM-VoiceAssistant /app/MagicMirror/modules/MMM-VoiceAssistant
COPY ./MagicMirror/config/config.js /app/MagicMirror/config/config.js

# Expose ports
EXPOSE 8080 5000

# Create startup script
RUN echo '#!/bin/bash\n\
cd /app/face_recognition && python3 main.py &\n\
cd /app/MagicMirror && npm run start\n\
' > /app/start.sh && chmod +x /app/start.sh

# Set environment variables
ENV DISPLAY=:0
ENV NODE_ENV=production

# Start services
CMD ["/app/start.sh"]
