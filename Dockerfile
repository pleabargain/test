FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY src/ src/
COPY words.csv .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Set environment variable
ENV PORT=8080

# Run the application with explicit host binding
CMD ["python", "-u", "main.py"]
