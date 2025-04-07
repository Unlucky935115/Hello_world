from loguru import logger

logger.add("execution_logs/loguru_sample.log")

def logs_sample():
    logger.trace("This is a TRACE Message")
    logger.debug("This is a DEBUG Message")
    logger.info("This is a INFO Message")
    logger.success("This is a SUCCCESS Message")
    logger.warning("This is a WARNING Message")
    logger.error("This is a ERROR Message")
    logger.critical("This is a CRITICAL Message")

logs_sample()
