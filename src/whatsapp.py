from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_whatsapp_web(driver: webdriver.Chrome):
    """Open WhatsApp Web and wait for login."""
    driver.get("https://web.whatsapp.com")
    print("WhatsApp Web opened. Waiting for login...")
    
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@data-tab="3"]')))
    print("✅ Logged in successfully!")


def search_group(driver: webdriver.Chrome, group_name: str):
    """Search for the specified WhatsApp group."""
    print(f"🔍 Searching for group: {group_name}")
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.click()
    search_box.send_keys(group_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)