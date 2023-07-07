import pytest
from selenium import webdriver

from web_tests.browser import log_screenshot

@pytest.mark.web
@pytest.mark.rp
def test_basic_options():
    # Create a WebDriver instance
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    # Navigate to a webpage
    driver.get("https://www.example.com")

    log_screenshot(driver)

    # Close the WebDriver instance
    driver.quit()



