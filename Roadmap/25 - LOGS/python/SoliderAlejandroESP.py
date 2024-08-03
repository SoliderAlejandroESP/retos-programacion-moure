import logging

"""
Ejercicio
"""

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

logging.debug("Esto es un mensaje de DEBUG")
logging.info("Esto es un mensaje de INFO")
logging.warning("Esto es un mensaje de WARNING")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de CRITICAL")