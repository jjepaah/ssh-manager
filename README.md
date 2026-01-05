# ssh-manager
Terminal tool to ssh connection and saved connections manager

main.py                     : Entry point of tool
connection_manager.py       : Handles fetching saved connections from file and provides options
ssh_utils.py                : Contains utility functions for establishing SSH connections


=== Main ===
This script uses the `argparse` library to parse command-line arguments, specifically the path to the file containing saved connections. It then enters a loop where it
displays options for saved connections and prompts the user to choose one or create a new connection.

For each chosen connection, it establishes an SSH session using the `ssh_utils` module and executes a simple command (`ls -l`) on the remote host.

=== Connection manager ===
This class loads the saved connections from a JSON file and provides methods to get all saved connections and retrieve details for a specific connection.

=== SSH utils ===
This module contains a utility function to establish an SSH connection using the `paramiko` library.