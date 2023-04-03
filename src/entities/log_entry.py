from datetime import datetime

class LogEntry:
    def __init__(self, user: str, logtitle: str, logdate: datetime):
        self.user = user
        self.logtitle = logtitle
        self.logdate = logdate

    