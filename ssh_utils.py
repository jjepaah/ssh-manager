import paramiko

def establish_ssh_connection(host, username=None, password=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if username and password:
        ssh.connect(hostname=host, username=username, password=password)
    elif username:
        key = paramiko.RSAKey.from_private_key_file("/path/to/private/key")
        ssh.connect(hostname=host, username=username, pkey=key)
    else:
        raise ValueError("Either username or password must be provided")
    return ssh