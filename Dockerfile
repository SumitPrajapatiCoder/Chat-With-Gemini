# Dockerfile

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy all project files and .env
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply migrations automatically on container start
CMD ["sh", "-c", "python manage.py migrate && gunicorn gemini_project.wsgi:application --bind 0.0.0.0:8000"]

EXPOSE 8000
