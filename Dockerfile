FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY main.py .
COPY ./app ./app

# Copy the locally downloaded model
COPY ./models/all-MiniLM-L6-v2 ./models/all-MiniLM-L6-v2

# Set environment variable to run sentence-transformers in offline mode
ENV SENTENCE_TRANSFORMERS_HOME=/app/models

CMD ["python", "main.py"]
