# Flask Web App

## Docker Hub Deployment

1. Create Docker Hub account at hub.docker.com
2. Create access token in Docker Hub (Account Settings > Security)
3. Add GitHub secrets:
   - DOCKERHUB_USERNAME
   - DOCKERHUB_TOKEN

4. Push to main branch to trigger automatic build and publish

To use:
```
docker pull your-username/repository-name
docker run -p 8080:8080 your-username/repository-name
```

## Local Docker

```
docker build -t word-explorer .
docker run -p 8080:8080 word-explorer
```

## Files
- main.py - Flask app
- Dockerfile - Container config
- .github/workflows/docker-publish.yml - CI/CD
- src/index.html - Frontend
- words.csv - Data
