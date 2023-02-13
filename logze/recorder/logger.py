import requests
from pymongo import MongoClient
from models.log import Log


class LogRecorder:
    """Attributes:
    mongo_uri (str): MongoDB connection string.
    db_name (str): MongoDB database name.
    logs_collection_name (str): Name of collection to record data.
    teams_webhook (str): Microsoft Teams webhook url to send error logs in a channel.
    """

    def __init__(
        self,
        mongo_uri: str,
        db_name: str,
        logs_collection_name: str,
        teams_webhook=None,
    ):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.logs_collection_name = logs_collection_name
        self.teams_webhook = teams_webhook

    def record_log(self, log: Log):
        """Record the log into MongoDB
        Attributes:
            log (Log): Log object.
        """
        client = MongoClient(self.mongo_uri)
        db = client[self.db_name]
        logs_collection = db[self.logs_collection_name]
        logs_collection.insert_one(log.__dict__)
        client.close()

        if log.level == "error" and self.teams_webhook is not None:
            url = self.teams_webhook
            headers = {"Content-Type": "application/json"}
            payload = {
                "@type": "MessageCard",
                "@context": "http://schema.org/extensions",
                "summary": "Log message",
                "themeColor": "ff0000",
                "title": f"Log: {log.source}",
                "text": str(log.timestamp) + " " + log.message,
            }
            requests.post(url, headers=headers, json=payload)
