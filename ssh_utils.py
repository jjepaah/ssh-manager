import paramiko

def establish_ssh_connection(host, username=None, password=None, private_key_path=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if private_key_path:
        key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh.connect(hostname=host, pkey=key)
    elif username and password:
        ssh.connect(hostname=host, username=username, password=password)
    else:
        raise ValueError("Either private key path or a combination of username/password must be provided")
    return ssh