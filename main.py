import logging
from typing import Optional
from src.driver import setup_chrome_driver, close_driver
from src.whatsapp import open_whatsapp_web, search_group
from src.message import send_message
from src.poll import create_poll
from config.settings import WhatsappConfig
import time
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_config() -> bool:
    """Validate the configuration settings."""
    if not os.path.exists(WhatsappConfig.PROFILE_PATH):
        logger.error(f"Chrome profile path does not exist: {WhatsappConfig.PROFILE_PATH}")
        return False
    if not WhatsappConfig.GROUP_NAME:
        logger.error("Group name is not configured")
        return False
    return True

def main():
    """Main function to execute the WhatsApp automation."""
    if not validate_config():
        return

    driver: Optional[webdriver.Chrome] = None
    try:
        logger.info("Setting up Chrome driver...")
        driver = setup_chrome_driver(WhatsappConfig.PROFILE_PATH)
        
        logger.info("Opening WhatsApp Web...")
        open_whatsapp_web(driver)
        
        logger.info(f"Searching for group: {WhatsappConfig.GROUP_NAME}")
        if not search_group(driver, WhatsappConfig.GROUP_NAME):
            logger.error(f"Group '{WhatsappConfig.GROUP_NAME}' not found")
            return

        while True:
            message = input("Enter the message to send (or 'exit' to quit): ").strip()
            if message.lower() == "exit":
                break
            if not message:
                logger.warning("Empty message, skipping...")
                continue
                
            try:
                send_message(driver, message)
                logger.info("Message sent successfully")
            except Exception as e:
                logger.error(f"Failed to send message: {str(e)}")
                
        time.sleep(5)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        if driver:
            logger.info("Closing Chrome driver...")
            close_driver(driver)

if __name__ == "__main__":
    main()