import argparse
from connection_manager import ConnectionManager
from ssh_utils import establish_ssh_connection

def main():
    parser = argparse.ArgumentParser(description='SSH Manager')
    parser.add_argument('--file-path', help='Path to file containing saved connections')
    args = parser.parse_args()

    if not args.file_path:
        print("Error: --file-path is required")
        return 1

    connection_manager = ConnectionManager(args.file_path)

    while True:
        print("\nOptions:")
        for i, connection_name in enumerate(connection_manager.get_saved_connections()):
            print(f"{i+1}. {connection_name}")

        choice = input("Enter the number of your chosen connection, or 'n' to create a new one: ")
        if choice.lower() == 'n':
            # Create a new connection
            host = input("Host: ")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            private_key = None  # For now, assume no private key is used

            ssh = establish_ssh_connection(host, username, password=password)
            # Save the new connection to file
            connection_name = input("Name for this connection: ")
            connection_manager.connections[connection_name] = {
                'host': host,
                'username': username,
                'password': password,
                'private_key': private_key
            }
            with open(args.file_path, 'w') as f:
                json.dump(connection_manager.connections, f)

        else:
            try:
                connection_index = int(choice) - 1
                if connection_index < len(connection_manager.get_saved_connections()):
                    connection_name = connection_manager.get_saved_connections()[connection_index]
                    details = connection_manager.get_connection_details(connection_name)
                    host = details['host']
                    username = details['username']
                    password = details['password']

                    ssh = establish_ssh_connection(host, username, password=password)

                    # Establish SSH session and execute commands
                    stdin, stdout, stderr = ssh.exec_command('ls -l')
                    print(stdout.read().decode())
                else:
                    print("Invalid connection number")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    main()