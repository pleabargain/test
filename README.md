# Flask Web App Starter

A Flask starter template as per [these docs](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application).

## Getting Started

Previews should run automatically when starting a workspace.


Deploy to Render.com (Easiest Method):

Create account at render.com

Create new Web Service

Connect your repository

Set build command: pip install -r requirements.txt

Set start command: gunicorn main:app

Choose free plan

Click Deploy

Deploy with Docker (Any cloud platform):

Build: docker build -t word-explorer .

Run: docker run -p 8080:8080 word-explorer

The application is ready for deployment with:

Production-ready Flask configuration

Dockerfile for containerization

Gunicorn for production server

Environment variable support for cloud platforms

Required dependencies in requirements.txt

Files prepared for deployment:

main.py - Flask application with production settings

requirements.txt - Dependencies (Flask, Gunicorn)

Dockerfile - Container configuration

src/index.html - Frontend interface

words.csv - Word database

Choose either Render.com for simple deployment or Docker for more flexibility. The application will work the same way in both environments, providing word search, synonyms/antonyms lookup, and favorite word management functionality.