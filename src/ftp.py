import pysftp

def send(ftp_hostname, ftp_user, ftp_password, ftp_dir, xml_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  
    with pysftp.Connection(host=ftp_hostname, username=ftp_user, password=ftp_password, cnopts=cnopts) as sftp:
        with sftp.cd(ftp_dir):
            sftp.put(xml_path)