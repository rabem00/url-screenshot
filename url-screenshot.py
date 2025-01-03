#!/usr/bin/env python
#
# Author: M. Rabelink
# Date: 2024-12-16
# Description: take screenshot from url 
#
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def take_screenshot(url, output_file):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    # Initialize the Chrome driver
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Set window size
        driver.set_window_size(1920, 1080)
        
        # Navigate to URL
        driver.get(url)
        
        # Wait for page to load (adjust if needed)
        time.sleep(5)
        
        # Take screenshot
        driver.save_screenshot(f"/app/screenshots/{output_file}")
        print(f"Screenshot saved as {output_file}")
        
    except Exception as e:
        print(f"Error taking screenshot: {str(e)}")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 url-screenshot.py <url> <output_file.png>")
        sys.exit(1)
        
    url = sys.argv[1]
    output_file = sys.argv[2]
    take_screenshot(url, output_file)