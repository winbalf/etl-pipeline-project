# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y \
  gcc \
  libpq-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]