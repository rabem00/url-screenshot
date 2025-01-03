# URL Screenshot Docker Application

A containerized application that takes screenshots of web pages using Selenium and Chromium in a Docker container. Perfect for automated webpage capturing and monitoring through cron jobs.

## Features

- Headless browser automation using Selenium and Chromium
- Docker containerization for consistent environment and easy deployment
- Support for custom screenshot resolutions (default: 1920x1080)
- Volume mounting for easy access to screenshots
- Suitable for cron job automation
- Cross-platform compatibility

## Prerequisites

- Docker installed on your system
- Basic understanding of Docker commands
- Sufficient disk space for screenshots
- Internet connection for accessing web pages

## Installation

1. Clone or create a new directory for the project:
```bash
mkdir screenshot-project
cd screenshot-project
```

2. Create the following files in your project directory:
- `Dockerfile`
- `requirements.txt`
- `url-screenshot.py`

3. Build the Docker image:
```bash
docker build -t url-screenshot .
```

## Usage

### Basic Usage
Take a screenshot of a single URL:
```bash
docker run -v $(pwd)/screenshots:/app/screenshots url-screenshot "https://example.com" "output.png"
```

### Parameters
- First argument: Target URL
- Second argument: Output filename (must end in .png)

### Output
Screenshots are saved to the mounted `/screenshots` directory on your host machine.

## Customization

### Modifying Screenshot Resolution
Edit `url-screenshot.py` and change the following line:
```python
driver.set_window_size(1920, 1080)  # Modify dimensions as needed
```

### Adjusting Page Load Time
Edit `url-screenshot.py` and modify the sleep duration:
```python
time.sleep(5)  # Adjust number of seconds as needed
```
