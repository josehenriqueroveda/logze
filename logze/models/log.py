from datetime import datetime


class Log:
    """Attributes:
    source (str): Source project/file of the log.
    level (str): 'info', 'warn' or 'error'.
    message (str): Log detailed message.
    event (str): Event where the log was triggered.
    """

    def __init__(self, source: str, level: str, message: str, event: str):
        self.source = source
        self.timestamp = str(datetime.now())
        self.level = level.lower()
        self.message = message
        self.event = function
