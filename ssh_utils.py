import subprocess

def establish_ssh_connection(host, username=None, password=None, private_key_path=None):
    command = "ssh " + host
    subprocess.run(command, shell=True)
    


def execute_command(ssh, command):
    transport = ssh.get_transport()
    channel = transport.open_session()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    stdin.write(command.encode())
    stdin.flush()

    output = stdout.read().decode()
    exit_status = channel.recv_exit_status()

    return output, exit_status

    ssh = establish_ssh_connection(host)
    if ssh:
        command = 'ls -l'
        output, exit_status = execute_command(ssh, command)
        print(output)
