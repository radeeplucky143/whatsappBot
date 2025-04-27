from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.utils.logger import setup_logger
from src.config.settings import WhatsappConfig

logger = setup_logger(__name__)

class MessageManager:
    """Manages message sending functionality."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WhatsappConfig.ELEMENT_TIMEOUT)
    
    def send(self, message: str) -> bool:
        """Send a message to the current chat."""
        try:
            if len(message) > WhatsappConfig.MAX_MESSAGE_LENGTH:
                logger.warning(f"Message exceeds maximum length ({WhatsappConfig.MAX_MESSAGE_LENGTH} characters)")
                return False
            
            # Find and click the message input box
            message_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WhatsappConfig.ELEMENTS['message_input']))
            )
            message_box.click()
            
            # Type the message
            message_box.send_keys(message)
            
            # Find and click the send button
            send_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, WhatsappConfig.ELEMENTS['send_button']))
            )
            send_button.click()
            
            logger.info("Message sent successfully")
            return True
            
        except TimeoutException:
            logger.error("Timeout while sending message")
            return False
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            return False 