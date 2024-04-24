import os
from dotenv import load_dotenv
import src.bearer_token as bearer_token
import src.data as _data
import src.xml as xml
import src.utils as utils
import src.ftp as ftp
import sys
import argparse
from datetime import datetime

load_dotenv()

API_URL = os.getenv('API_URL')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')
FTP_HOSTNAME= os.getenv('FTP_HOSTNAME')
FTP_USER= os.getenv('FTP_USER')
FTP_PASSWORD= os.getenv('FTP_PASSWORD')
FTP_DIR= os.getenv('FTP_DIR')
SENDERNR= os.getenv('SENDERNR')
SENDERNAME= os.getenv('SENDERNAME')
RECEIVERNR= os.getenv('RECEIVERNR')
RECEIVERNAME= os.getenv('RECEIVERNAME')
BASE_FILENAME= os.getenv('BASE_FILENAME')

NOW = datetime.now()

def main():
    env_vars = ['API_URL', 'API_USERNAME', 'API_PASSWORD', 'FTP_HOSTNAME', 'FTP_USER', 'FTP_PASSWORD']
    missing_vars = [var for var in env_vars if os.getenv(var) is None]
    if missing_vars:
        print(f"Missing environment variables: {', '.join(missing_vars)}. Make sure they are set in the .env file.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--start_date', default=NOW.strftime('%Y-%m-%d'), help='Start date (default is today)')
    parser.add_argument('--end_date', default=None, help='End date (default is None)')
    parser.add_argument('--days', type=int, default=25, help='Number of days to add to start date (default is 25).')
    parser.add_argument('--send_ftp', type=int, default=1, help='Send to ftp (default is 1 (true)).')
    args = parser.parse_args()

    if args.days and args.end_date:
        print(f"Can't specify --days and --end_date simultaneously.")
        sys.exit(1)

    start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    days = args.days

    end_date = utils.calculate_end_date(start_date, days)

    token = bearer_token.get(API_USERNAME, API_PASSWORD, API_URL)

    data = _data.get(API_URL, token, start_date, end_date)

    _xml = xml.create(data, SENDERNR, SENDERNAME, RECEIVERNR, RECEIVERNAME, start_date, end_date, BASE_FILENAME)

    if args.send_ftp == 1:
        ftp.send(FTP_HOSTNAME, FTP_USER, FTP_PASSWORD, FTP_DIR, _xml)

if __name__ == "__main__":
    main()