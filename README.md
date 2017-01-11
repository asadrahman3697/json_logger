# json_logger
What is it about?
----------------
This repository contains code and configuration to setup centralised logging. The logger allows for all code in a codebase to take advantage of logging, by simply importing the module and referring to it when carrying out any logging function.

How does it work?
-----------------
1.  The logger module user a json configuration file to setup the required configuration. This allows the logging structure to be stored in a json file, independent of the code.
2. The logger is imported in any code that requires logging / debugging. Use this instead of print statements!
3. Logs can be seen on console output and written to file as well.
4. Logging can be disabled in the code, without having to remove the calling commands

How to use the code?
--------------------
1. Download the code (logger.py) and the json file(logger.json)
2. In your code type:

from logger import Logger

# Create the logger 
# The parameters are 
# logfile=True (default is False) - to turn on logging to file, the filename, format and levels are in the json file
# disable=True (default is False) - to disable all logging
logger = Logger() 

# Start using the logger
logger.info('Start of Program')
logger.debug("Some bug check1")
logger.warnings("Might be serious one day")
logger.critical("Ouch! This is serious")

