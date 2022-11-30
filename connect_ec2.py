import paramiko
import pandas as pd
from keys import information
key = paramiko.RSAKey.from_private_key_file("usr/563186832/Downloads/key.pem")

transport = paramiko.Transport((host, port))

transport.connect(username="zl369", pkey=key) # you may change it with your own key to use the whole app

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get(remote_path , local_path) # host, port, transport, and remote path are in the github secrets (this is used to connect aws so it is in github
                                    # for later I push it into lambda, they should be saved in AWS secret)