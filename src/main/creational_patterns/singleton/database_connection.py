import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("This class is a singleton!")
        self.connection = self._connect_to_db()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    def _connect_to_db(self):
        # Simulate DB connection
        return "Connected to database"
