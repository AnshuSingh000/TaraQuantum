import logging
import sys

def setup_logger(name="TARA"):
    """
    Sets up a professional logging system.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        # Create console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        
        # Create formatter (Time - Level - Message)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
    return logger