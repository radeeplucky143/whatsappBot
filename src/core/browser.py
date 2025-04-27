from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

from src.utils.logger import setup_logger
from src.config.settings import WhatsappConfig

logger = setup_logger(__name__)

class BrowserManager:
    """Manages the Chrome browser instance and its lifecycle."""
    
    def __init__(self, profile_path: str):
        self.profile_path = profile_path
        self.driver: Optional[webdriver.Chrome] = None
    
    def setup(self) -> bool:
        """Set up the Chrome browser with the specified profile."""
        try:
            chrome_options = Options()
            
            # Add all Chrome options from settings
            for option, value in WhatsappConfig.get_chrome_options().items():
                chrome_options.add_argument(f"{option}={value}")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(WhatsappConfig.ELEMENT_TIMEOUT)
            self.driver.set_page_load_timeout(WhatsappConfig.PAGE_LOAD_TIMEOUT)
            
            logger.info("Chrome browser setup completed successfully")
            return True
            
        except WebDriverException as e:
            logger.error(f"Failed to setup Chrome browser: {str(e)}")
            return False
    
    def close(self) -> None:
        """Close the browser and clean up resources."""
        if self.driver:
            try:
                self.driver.quit()
                logger.info("Browser closed successfully")
            except Exception as e:
                logger.error(f"Error while closing browser: {str(e)}")
            finally:
                self.driver = None 