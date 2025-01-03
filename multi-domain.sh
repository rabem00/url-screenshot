#!/bin/bash
SCREENSHOTS_DIR="/path/to/screenshots"
DATE_STAMP=$(date +%Y%m%d_%H%M)

# List of URLs to screenshot
URLS=(
    "https://example1.com"
    "https://example2.com"
    "https://example3.com"
)

for url in "${URLS[@]}"; do
    # Extract domain name for filename
    domain=$(echo $url | sed -e 's/https\?:\/\///' -e 's/\/.*//' -e 's/[^a-zA-Z0-9]/_/g')
    docker run -v $SCREENSHOTS_DIR:/app/screenshots url-screenshot "$url" "${domain}_${DATE_STAMP}.png"
done