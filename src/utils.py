import logging
import os

def setup_logging():
    """Configure logging for the application."""
    log_level = logging.DEBUG if os.getenv("FLASK_DEBUG", "False").lower() == "true" else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("juns_clinic.log"),
            logging.StreamHandler()
        ]
    )
