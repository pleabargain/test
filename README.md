# Word Machine Flask App

## Docker Hub Deployment

### For Users
To run the application:
```bash
docker pull pleabargain/word-machine:latest
docker run -p 8080:8080 pleabargain/word-machine:latest
```

Then open http://localhost:8080 in your browser.

### For Developers
1. Create Docker Hub account at hub.docker.com
2. Create access token in Docker Hub:
   - Go to Account Settings > Security
   - Click "New Access Token"
   - Save the token

3. Add GitHub secrets:
   - Go to your repository Settings > Secrets > Actions
   - Add two secrets:
     - DOCKERHUB_USERNAME: your Docker Hub username
     - DOCKERHUB_TOKEN: your Docker Hub access token

4. Push to main branch to trigger automatic build and publish

## Local Development
Build and run locally:
```bash
docker build -t word-machine .
docker run -p 8080:8080 word-machine
```

## Project Files
- main.py - Flask application
- Dockerfile - Container configuration
- .github/workflows/docker-publish.yml - Docker Hub automation
- src/index.html - Frontend interface
- words.csv - Word database
- requirements.txt - Python dependencies
