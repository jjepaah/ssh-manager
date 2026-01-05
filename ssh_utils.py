import paramiko

def establish_ssh_connection(host, username, password=None, private_key=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if private_key:
        key = paramiko.RSAKey.from_private_key_file(private_key)
        ssh.connect(hostname=host, username=username, pkey=key)
    elif password:
        ssh.connect(hostname=host, username=username, password=password)
    else:
        raise ValueError("Either password or private_key must be provided")
    return ssh