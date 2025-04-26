from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def create_poll(driver, question, options):
    print("📊 Creating poll...")

    # --- Wait for chat to open ---
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-testid="conversation-compose-box-input"]'))
    )
    print("🧹 Chat screen loaded, proceeding to create poll.")

    # Click the 📎 attachment icon
    attach_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="clip"]'))
    )
    attach_btn.click()
    print("📎 Attach button clicked.")

    # Wait for attachment menu to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[1]'))
    )

    # Click the 🗳️ Poll button (within the footer)
    poll_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Poll"]'))
    )
    poll_btn.click()
    print("🗳️ Poll button clicked.")

    # Fill poll question
    question_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-testid="poll-compose-question"]//div[@contenteditable="true"]'))
    )
    question_box.click()
    question_box.send_keys(question)
    print(f"❓ Poll Question: {question}")

    # Fill poll options
    for i, option in enumerate(options):
        option_input_xpath = f'(//div[@data-testid="poll-compose-option"]//div[@contenteditable="true"])[{i+1}]'
        option_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, option_input_xpath))
        )
        option_box.click()
        option_box.send_keys(option)
        print(f"📝 Added Option {i+1}: {option}")
        time.sleep(0.5)

    # Click Send Poll
    send_button = driver.find_element(By.XPATH, '//span[@data-testid="send"]')
    send_button.click()
    print("✅ Poll sent successfully!")
