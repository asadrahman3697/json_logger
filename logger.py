#! python
import logging
import logging.config
import json


class Logger():
    
    def __new__(self, disable=False, logfile=False,
        logconfig='logging.json'):
        
        if disable:
            logging.disable(logging.CRITICAL) # Disable logging
                    
        with open(logconfig, 'r') as f:
           logging_config = json.load(f)
        logging.config.dictConfig(logging_config)
        
        loggername = __name__
        if logfile:
            loggername += '_filewriter' 
                
        self.custom_logger = logging.getLogger(loggername)
       
        return self.custom_logger            
