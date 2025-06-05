### What is Paramiko?
Paramiko is a Python library that allows you to:
1. Connect to remote machines over SSH (Secure Shell)
2. Execute commands, transfer files, and automate tasks securely.

> It uses Python implementations of SSHv2 protocol to create encrypted sessions to remote machines.<br>

#### What Can You Do With Paramiko?
1. Automate SSH logins (no manual password typing)
2. Run shell commands remotely
3. Transfer files via SFTP
4. Create tunnels or port forwarding

#### Under the Hood: How Paramiko Works

1. Socket Connection (TCP Layer)
Paramiko first creates a raw socket connection to the remote host on port 22 (default SSH port).

```python
import paramiko
client = paramiko.SSHClient()
# Internally:
socket.create_connection((hostname, port))
```

2. SSH Handshake & Key Exchange
Once the socket is open, Paramiko initiates an SSH handshake, following SSHv2 protocol:
> 1. Exchange keys
> 2. Negotiate encryption algorithms
Verify server’s identity using its host key
```python
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```

3. Authentication
```python
client.connect(hostname, username='user', password='secret')
# OR
client.connect(hostname, username='user', key_filename='~/.ssh/id_rsa')
```

4. Channel Creation
Once authenticated, it opens a channel over the SSH session.
Channels can be used to:
1. Run shell commands
2. Start SFTP session

```python
stdin, stdout, stderr = client.exec_command('ls -l')
```
5. Execute Commands or Transfer Files
Paramiko sends the command through the SSH channel. It reads the output and error streams
```python
print(stdout.read().decode())
``` 
For file transfer:

```python
sftp = client.open_sftp()
sftp.put('local.txt', '/remote/path/remote.txt')
```
6. Cleanup and Close
Properly closes the channel and socket
```python
client.close()
```
#### Example Use Case: Automating Remote Task
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.10', username='user', password='pass')

stdin, stdout, stderr = ssh.exec_command('uptime')
print(stdout.read().decode())

ssh.close()
```


### final code:
```python
import paramiko

# Create object of SSHClient and 
# connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local 
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('1.1.1.2', port=22, username='UserName',
            password='PassWord', timeout=3)

# Execute command on SSH terminal 
# using exec_command
stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
```