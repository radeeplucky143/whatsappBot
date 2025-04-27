import os
from pathlib import Path
from typing import Optional

class WhatsappConfig:
    """Configuration settings for WhatsApp Bot."""
    
    # WhatsApp Configuration
    GROUP_NAME: str = os.getenv("WHATSAPP_GROUP_NAME", "whatsapp Testing")
    WHATSAPP_WEB_URL: str = "https://web.whatsapp.com"
    
    # Browser Configuration
    DEFAULT_PROFILE_PATH = Path.home() / ".whatsapp_chrome_profile"
    PROFILE_PATH: str = os.getenv("CHROME_PROFILE_PATH", str(DEFAULT_PROFILE_PATH))
    
    # Timeout Settings (in seconds)
    PAGE_LOAD_TIMEOUT: int = 30
    ELEMENT_TIMEOUT: int = 10
    
    # Message Settings
    MAX_MESSAGE_LENGTH: int = 4096
    
    # Browser Options
    CHROME_OPTIONS: dict = {
        'disable_gpu': True,
        'no_sandbox': True,
        'disable_dev_shm_usage': True,
        'start_maximized': True,
        'disable_infobars': True,
        'disable_notifications': True
    }
    
    # WhatsApp Web Elements
    ELEMENTS = {
        'chat_list': "div[data-testid='chat-list']",
        'search_input': "div[data-testid='chat-list-search']",
        'search_box': "div[data-testid='chat-list-search'] input",
        'message_input': "div[data-testid='conversation-compose-box-input']",
        'send_button': "span[data-testid='send']",
        'group_title': "//span[@title='{}']"
    }
    
    @classmethod
    def validate(cls) -> bool:
        """Validate the configuration settings."""
        try:
            # Validate group name
            if not cls.GROUP_NAME or not isinstance(cls.GROUP_NAME, str):
                raise ValueError("Invalid group name configuration")
            
            # Validate profile path
            if not os.path.exists(cls.PROFILE_PATH):
                os.makedirs(cls.PROFILE_PATH, exist_ok=True)
            
            # Validate timeouts
            if not isinstance(cls.PAGE_LOAD_TIMEOUT, int) or cls.PAGE_LOAD_TIMEOUT <= 0:
                raise ValueError("Invalid page load timeout configuration")
            
            if not isinstance(cls.ELEMENT_TIMEOUT, int) or cls.ELEMENT_TIMEOUT <= 0:
                raise ValueError("Invalid element timeout configuration")
            
            # Validate message settings
            if not isinstance(cls.MAX_MESSAGE_LENGTH, int) or cls.MAX_MESSAGE_LENGTH <= 0:
                raise ValueError("Invalid max message length configuration")
            
            return True
            
        except Exception as e:
            print(f"Configuration validation failed: {str(e)}")
            return False
    
    @classmethod
    def get_chrome_options(cls) -> dict:
        """Get Chrome options as a dictionary."""
        return {
            '--user-data-dir': cls.PROFILE_PATH,
            **{f'--{k.replace("_", "-")}': str(v).lower() 
               for k, v in cls.CHROME_OPTIONS.items()}
        } 