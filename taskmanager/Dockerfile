# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

RUN mkdir -p /app/staticfiles

# Collect static files (for production)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "taskmanager.wsgi:application"]