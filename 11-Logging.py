"""
5 Securities Levels:
DEBUG -> Developers to know, Troubleshoot, Debugging
INFO -> All informational msgs, just to know
WARNING -> System didnt crash, but may happen something
ERROR -> Classical Exception, Could not do something
CRITICAL -> Stopped, Immediate atention
"""

import logging

#
# Define o nível de atenção
#

logging.basicConfig(level=logging.INFO) 

logging.warning("You have got 20 mails in your email")
logging.critical("All components failed")

logger = logging.getLogger("NeuralNine Logger")
logger.info("The best logger was created")
logger.critical("YT Channel deleted!")

# Define um arquivo de log
handler = logging.FileHandler("mylog.log")
# define nivel para arquivo de log
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")