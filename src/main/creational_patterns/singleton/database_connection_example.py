class DatabaseConnection:
    _instance = None


    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        # Logic for creating a database connection
        return "Database Connection Established"

    def get_connection(self):
        return self.connection


# Testing DatabaseConnection Singleton
db1 = DatabaseConnection()
print(db1.get_connection())  # Output: Database Connection Established

db2 = DatabaseConnection()
print(db2.get_connection())  # Output: Database Connection Established (same connection)

print(db1 is db2)  # Output: True (db1 and db2 are the same instance)
