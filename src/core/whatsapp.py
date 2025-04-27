from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from src.utils.logger import setup_logger
from src.config.settings import WhatsappConfig

logger = setup_logger(__name__)

class WhatsAppManager:
    """Manages WhatsApp Web interactions."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WhatsappConfig.ELEMENT_TIMEOUT)
    
    def open_web(self) -> bool:
        """Open WhatsApp Web and wait for QR code scan."""
        try:
            self.driver.get(WhatsappConfig.WHATSAPP_WEB_URL)
            logger.info("Opened WhatsApp Web")
            
            # Wait for QR code to be scanned
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WhatsappConfig.ELEMENTS['chat_list']))
            )
            logger.info("QR code scanned successfully")
            return True
            
        except TimeoutException:
            logger.error("Timeout waiting for QR code scan")
            return False
        except Exception as e:
            logger.error(f"Error opening WhatsApp Web: {str(e)}")
            return False
    
    def search_group(self, group_name: str) -> bool:
        """Search for and select a WhatsApp group."""
        try:
            # Click on search input
            search_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WhatsappConfig.ELEMENTS['search_input']))
            )
            search_input.click()
            
            # Type group name
            search_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, WhatsappConfig.ELEMENTS['search_box']))
            )
            search_box.send_keys(group_name)
            
            # Wait for group to appear and click it
            group_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, WhatsappConfig.ELEMENTS['group_title'].format(group_name)))
            )
            group_element.click()
            
            logger.info(f"Group '{group_name}' selected successfully")
            return True
            
        except TimeoutException:
            logger.error(f"Timeout waiting for group '{group_name}'")
            return False
        except NoSuchElementException:
            logger.error(f"Group '{group_name}' not found")
            return False
        except Exception as e:
            logger.error(f"Error searching for group: {str(e)}")
            return False 