from src.driver import setup_chrome_driver, close_driver
from src.whatsapp import open_whatsapp_web, search_group
from src.message import send_message
from src.poll import create_poll
from config.settings import WhatsappConfig
import time

def main():
    """Main function to execute the WhatsApp automation."""
    driver = setup_chrome_driver(WhatsappConfig.PROFILE_PATH)
    
    try:
        open_whatsapp_web(driver)
        search_group(driver, WhatsappConfig.GROUP_NAME)
        message = input("Enter the message to send: ")
        while message != "exit":
            send_message(driver, message)
            message = input("Enter the message to send: ")
        time.sleep(5)
        
    finally:
        close_driver(driver)


if __name__ == "__main__":
    main()