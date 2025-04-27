import os
from typing import Optional
from pathlib import Path

class WhatsappConfig:
    # Get configuration from environment variables with fallback values
    GROUP_NAME: str = os.getenv("WHATSAPP_GROUP_NAME", "whatsapp Testing")
    
    # Use a default profile path in the user's home directory
    DEFAULT_PROFILE_PATH = Path.home() / ".whatsapp_chrome_profile"
    PROFILE_PATH: str = os.getenv("CHROME_PROFILE_PATH", str(DEFAULT_PROFILE_PATH))
    
    # WhatsApp Web URL
    WHATSAPP_WEB_URL: str = "https://web.whatsapp.com"
    
    # Timeout settings (in seconds)
    PAGE_LOAD_TIMEOUT: int = 30
    ELEMENT_TIMEOUT: int = 10
    
    # Message settings
    MAX_MESSAGE_LENGTH: int = 4096
    
    @classmethod
    def validate(cls) -> bool:
        """Validate the configuration settings."""
        if not cls.GROUP_NAME:
            return False
        if not os.path.exists(cls.PROFILE_PATH):
            os.makedirs(cls.PROFILE_PATH, exist_ok=True)
        return True