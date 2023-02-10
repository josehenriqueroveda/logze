from datetime import datetime

class Log():
    def __init__(self, job, level, message, function):
        self.job = job
        self.timestamp = str(datetime.now())
        self.level = level
        self.message = message
        self.function = function