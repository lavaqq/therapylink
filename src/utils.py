import sys
from datetime import date, datetime, timedelta

def format_data(data):
    print('format')

def calculate_end_date(start_date, days):
    date = start_date + timedelta(days=days)
    return date.strftime('%Y-%m-%d')

    
