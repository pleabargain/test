FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY src/ src/
COPY words.csv .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
