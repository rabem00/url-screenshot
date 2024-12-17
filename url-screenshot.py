#!/usr/bin/env python
#
# Author: M. Rabelink
# Date: 2024-13-12
# Description: take screenshot from url 
#
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def render_page(url, output_file):
    # run Chrome in headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # start a driver instance
    driver = webdriver.Chrome(options=options)
    try:
        # open the target website
        driver.get(url)

        # define a function to get scroll dimensions
        def get_scroll_dimension(axis):
            return driver.execute_script(f"return document.body.parentNode.scroll{axis}")

        # get the page scroll dimensions
        width = get_scroll_dimension("Width")
        height = get_scroll_dimension("Height")

        # set the browser window size
        driver.set_window_size(width, height)

        # get the full body element
        full_body_element = driver.find_element(By.TAG_NAME, "body")

        # take a full-page screenshot
        full_body_element.screenshot(output_file)
    finally:
        # quit the browser
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 selenium-screenshot.py <url> <output_file PNG>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    render_page(url, output_file)