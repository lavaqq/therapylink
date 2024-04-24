import pysftp

def send(ftp_hostname, ftp_user, ftp_password, ftp_dir, xml_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # This disables host key checking, which is not recommended in production
    try:
        with pysftp.Connection(host=ftp_hostname, username=ftp_user, password=ftp_password, cnopts=cnopts) as sftp:
            with sftp.cd(ftp_dir):
                sftp.put(xml_path)
        print('XML sent to FTP server.')
    except pysftp.CredentialException:
        print("Failed to log in to the FTP server. Please check your username and password.")
    except pysftp.ConnectionException:
        print("Could not connect to the FTP server. Please check the hostname and your network connection.")
    except Exception as e:
        print(f"An error occurred: {e}. Please check your .env variables and ensure all are correct.")