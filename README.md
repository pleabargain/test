# Word Machine Flask App

## Prerequisites

### Windows Users
1. Install Docker Desktop for Windows:
   - Download from https://www.docker.com/products/docker-desktop
   - During installation, ensure WSL 2 is enabled
   - Restart your computer after installation

2. Configure Docker Desktop:
   - Start Docker Desktop
   - Wait for Docker Desktop to fully start (check system tray icon)
   - Right-click Docker Desktop icon in system tray
   - Go to Settings > General
   - Ensure "Use WSL 2 based engine" is checked
   - Go to Settings > Resources > WSL Integration
   - Enable "Ubuntu" or your preferred WSL distribution
   - Click "Apply & Restart"

3. Verify Installation:
   ```powershell
   # Open PowerShell as Administrator and run:
   docker --version
   docker ps
   ```

### Linux Users
Install Docker using your package manager:

Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Log out and back in for changes to take effect
```

## Running the Application

1. Pull the image:
```bash
docker pull pleabargain/word-machine:latest
```

2. Run the container:
```bash
docker run -p 8080:8080 pleabargain/word-machine:latest
```

3. Access the application:
   - Open http://localhost:8080 in your browser

## Troubleshooting

### Windows Issues
If you see "error during connect: Post http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine...":

1. Restart Docker Desktop:
   - Right-click Docker Desktop icon
   - Select "Quit Docker Desktop"
   - Start Docker Desktop again
   - Wait for it to fully initialize

2. Reset Docker Desktop:
   ```powershell
   # Open PowerShell as Administrator
   wsl --shutdown
   net stop com.docker.service
   net start com.docker.service
   # Restart Docker Desktop
   ```

3. Check Windows Services:
   - Press Win+R, type "services.msc"
   - Find "Docker Desktop Service"
   - Ensure it's running
   - Restart if needed

### Linux Issues
If you see permission errors:
```bash
sudo chmod 666 /var/run/docker.sock
```

## Project Structure
- main.py - Flask application
- Dockerfile - Container configuration
- .github/workflows/docker-publish.yml - Docker Hub automation
- src/index.html - Frontend interface
- words.csv - Word database
- requirements.txt - Python dependencies
