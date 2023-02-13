import unittest
import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import sys
sys.path.append('../')
from models.log import Log


class TestLogRecording(unittest.TestCase):
    def setUp(self):
        mongo_uri = os.environ.get("MONGO_URI")
        db_name = os.environ.get("DB_NAME")
        if not mongo_uri:
            raise ValueError("MONGO_URI is not set")
        if not db_name:
            raise ValueError("DB_NAME is not set")

        self.test_db = MongoClient(mongo_uri)
        self.test_logs = self.test_db[db_name]

    def test_mongodb_connection(self):
        try:
            self.assertTrue(self.test_db)
        except ServerSelectionTimeoutError as e:
            self.fail(f"Failed to connect to MongoDB: {e}")

    def test_log_recording(self):
        log = Log("Log Unit Test", "info", "Test log", "test_log_recording")
        collection = self.test_logs["tests"]
        collection.insert_one(log.__dict__)
        recorded_log = collection.find_one(log.__dict__)
        self.assertEqual(log.__dict__, recorded_log)

    def test_delete_log(self):
        log = Log("Log Unit Test", "info", "Test log", "test_log_recording")
        collection = self.test_logs["tests"]
        collection.insert_one(log.__dict__)
        collection.delete_many({})
        recorded_logs = list(collection.find({}))
        self.assertEqual(len(recorded_logs), 0)


if __name__ == "__main__":
    unittest.main()
