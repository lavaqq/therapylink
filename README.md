```
# Therapylink

## Description

This project interfaces with specific APIs and FTP services to fetch, process, and transmit therapylink. It leverages environment variables to handle credentials and connection details securely, ensuring that sensitive data is not hardcoded into the source files.

## Getting Started

### Dependencies

- Python 3.x
- Requests
- Python-dotenv
- Argparse
- Datetime
- pysftp
- Additional dependencies are listed in the `requirements.txt` file.

### Installing

1. **Clone the repository**

   ```
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the root directory of your project and fill it with all necessary environment variables:

```plaintext
API_URL=your_api_url_here
API_USERNAME=your_api_username_here
API_PASSWORD=your_api_password_here
FTP_HOSTNAME=your_ftp_hostname_here
FTP_USER=your_ftp_username_here
FTP_PASSWORD=your_ftp_password_here
FTP_DIR=your_ftp_dir_here
SENDERNR=your_sender_number_here
SENDERNAME=your_sender_name_here
RECEIVERNR=your_receiver_number_here
RECEIVERNAME=your_receiver_name_here
BASE_FILENAME=your_base_filename_here
```

**Note:** Replace `your_*_here` with actual values required for your environment.

### Running the Program

To run the program, use the following command from the root directory:

```bash
python main.py
# or
python main.py --start_date YYYY-MM-DD --days 30
# or
python main.py --start_date YYYY-MM-DD --end_date YYYY-MM-DD 
```

- `--start_date`: The start date for the data processing (format: YYYY-MM-DD) (defaul is now()).
- `--end_date`: Optional, specify the end date for the data processing.
- `--days`: Number of days to add to the start date for calculating the end date (default is 25).

## Help

To get help and understand the usage of different arguments:

```bash
python main.py -h
```

## Authors

Contributors names and contact info

- **lavaqq** - *Initial work* - [email](mailto:mlava@tuta.io)
```
