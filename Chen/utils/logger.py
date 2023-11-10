import logging


def get_logger(loggerName: str = "run.log"):
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.INFO)

    logger = logging.getLogger(loggerName)
    logger.addHandler(streamHandler)

    return logger


logger = get_logger()
