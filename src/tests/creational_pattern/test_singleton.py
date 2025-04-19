import threading
from src.main.creational_patterns.singleton.database_connection import DatabaseConnection

def test_singleton_instance():
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()
    assert db1 is db2

def test_singleton_thread_safety():
    instances = []

    def create_instance():
        instances.append(DatabaseConnection.get_instance())

    thread1 = threading.Thread(target=create_instance)
    thread2 = threading.Thread(target=create_instance)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    assert instances[0] is instances[1]
