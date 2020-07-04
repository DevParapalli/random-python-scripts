import logging
logging.basicConfig(filename='logfile.log',format='%(levelname)s:%(message)s' ,level=logging.DEBUG) #DEBUG, INFO, WARNING, ERROR, CRITCAL
# use the next line iff the current run is to be documented.
#logging.basicConfig(filename='logfile.log',format='%(Levelname)s:%(message)s' ,level=logging.DEBUG, filemode="w")

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')