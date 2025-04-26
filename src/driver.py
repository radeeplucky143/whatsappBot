from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_chrome_driver(profile_path: str):
    """Setup the Chrome driver with the specified profile."""
    options = Options()
    options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    return driver

def close_driver(driver: webdriver.Chrome):
    """Close the ChromeDriver."""
    driver.quit()