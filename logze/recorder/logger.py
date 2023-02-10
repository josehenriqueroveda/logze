import requests
from pymongo import MongoClient
from models.log import Log


class LogRecorder:
    def __init__(self, mongo_uri, db_name, logs_collection_name, teams_webhook=None):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.logs_collection_name = logs_collection_name
        self.teams_webhook = teams_webhook
    

    def record_log(self, log: Log):
        """Record the log into MongoDB"""
        client = MongoClient(self.mongo_uri)
        db = client[self.db_name]
        logs_collection = db[self.logs_collection_name]
        logs_collection.insert_one(log.__dict__)
        client.close()


        if log.level == "error" and self.teams_webhook is not None:
            url = self.teams_webhook
            headers = {
                "Content-Type": "application/json"
            }
            payload = {
                "@type": "MessageCard",
                "@context": "http://schema.org/extensions",
                "summary": "Log message",
                "themeColor": "ff0000",
                "title": f"Log: {log.job}",
                "text": log.message
            }
            requests.post(self.teams_webhook, headers=headers, json=payload)
