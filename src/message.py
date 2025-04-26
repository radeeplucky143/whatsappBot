from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_message(driver: webdriver.Chrome, message: str):
    """Send a message to the currently selected WhatsApp group."""
    print("💬 Sending message...")
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    print("✅ Message sent successfully!")