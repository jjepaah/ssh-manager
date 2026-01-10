import argparse
from connection_manager import ConnectionManager
from ssh_utils import establish_ssh_connection

def get_username():
    return input("Input username? (press Enter to skip): ")

def get_password():
    password = None
    while True:
        response = input("Input password? (press Enter to skip): ")
        if response.strip() == "":
            continue
        else:
            password = response
            break
    return password

def main():
    parser = argparse.ArgumentParser(description='SSH Manager')
    parser.add_argument('--file-path', help='Path to file containing saved connections')
    args = parser.parse_args()

    """
    if not args.file_path:
        print("Error: --file-path is required")
        return 1
    """

    while True:
        print("\nOptions:")

        if args.file_path:
            connection_manager = ConnectionManager(args.file_path)
            for i, connection_name in enumerate(connection_manager.get_saved_connections()):
                print(f"{i+1}. {connection_name}")
        else:
            print("No connections found")

        choice = input("Enter the number of your chosen connection, or 'n' to create a new one: ")
        if choice.lower() == 'n':
            # Create a new connection
            host = input("Host: ")
            username_input = get_username()
            private_key_path_input = input("Private key path (press Enter to skip): ")

            if private_key_path_input.strip() != "":
                try:
                    paramiko.RSAKey.from_private_key_file(private_key_path_input)
                    ssh = establish_ssh_connection(host, private_key=private_key_path_input)
                except Exception as e:
                    print(f"Error reading private key file: {e}")
                    continue
            elif username_input == "":
                ssh = establish_ssh_connection(host)
            else:
                password_input = get_password()
                ssh = establish_ssh_connection(host, username=username_input or None, password=password_input)
        else:
            try:
                connection_index = int(choice) - 1
                if connection_index < len(connection_manager.get_saved_connections()):
                    connection_name = connection_manager.get_saved_connections()[connection_index]
                    details = connection_manager.get_connection_details(connection_name)
                    host = details['host']
                    username = details.get('username') or None
                    password = details.get('password')
                    private_key_path = details.get('private_key_path')

                    if not username and not password:
                        ssh = establish_ssh_connection(host)
                    else:
                        ssh = establish_ssh_connection(host, username, password=password, private_key=private_key_path)

                    if ssh:
                        # Establish SSH session and execute commands
                        stdin, stdout, stderr = ssh.exec_command('ls -l')
                        print(stdout.read().decode())
                else:
                    print("Invalid connection number")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    main()
