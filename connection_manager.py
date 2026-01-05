import json

class ConnectionManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.connections = self.load_connections()

    def load_connections(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.loads(f.read())
        except FileNotFoundError:
            return {}

    def get_saved_connections(self):
        return list(self.connections.keys())

    def get_connection_details(self, connection_name):
        return self.connections.get(connection_name)