
from logger import Logger
from datetime import datetime
if __name__ == "__main__":
    
    logger = Logger()
        
    logger.debug(datetime.now(),"This is a debug message")
        
    logger.info(datetime.now(),"Application started successfully")
        
    logger.warning(datetime.now(),"Disk space is running low")
        
    logger.error(datetime.now(),"Database connection failed")
        
    logger.fatal(datetime.now(),"System encountered unrecoverable error")
        
    