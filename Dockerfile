# Dockerfile
FROM python:3.9-slim

# Install required packages including Chrome and ChromeDriver dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set display port to avoid crash
ENV DISPLAY=:99

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the screenshot script
COPY url-screenshot.py /app/
WORKDIR /app

# Create directory for screenshots
RUN mkdir -p /app/screenshots

# Set the entrypoint
ENTRYPOINT ["tail",  "-f", "url-screenshot.py"]
