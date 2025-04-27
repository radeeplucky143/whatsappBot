from src.core.browser import BrowserManager
from src.core.whatsapp import WhatsAppManager
from src.features.messaging import MessageManager
from src.config.settings import WhatsappConfig
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    """Main function to execute the WhatsApp automation."""
    # Initialize browser manager
    browser = BrowserManager(WhatsappConfig.PROFILE_PATH)
    
    try:
        # Setup browser
        if not browser.setup():
            logger.error("Failed to setup browser")
            return
        
        # Initialize WhatsApp manager
        whatsapp = WhatsAppManager(browser.driver)
        
        # Open WhatsApp Web
        if not whatsapp.open_web():
            logger.error("Failed to open WhatsApp Web")
            return
        
        # Search for group
        if not whatsapp.search_group(WhatsappConfig.GROUP_NAME):
            logger.error(f"Failed to find group: {WhatsappConfig.GROUP_NAME}")
            return
        
        # Initialize message manager
        messenger = MessageManager(browser.driver)
        
        # Message sending loop
        while True:
            message = input("Enter the message to send (or 'exit' to quit): ").strip()
            
            if message.lower() == "exit":
                break
                
            if not message:
                logger.warning("Empty message, skipping...")
                continue
            
            if not messenger.send(message):
                logger.error("Failed to send message")
                continue
                
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
    finally:
        browser.close()

if __name__ == "__main__":
    main() 