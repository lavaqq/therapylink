import sys
from datetime import date, datetime, timedelta
from fraction import Fraction

def format_data(data):
    print('format')

def calculate_end_date(start_date, days):
    date = start_date + timedelta(days=days)
    return date.strftime('%Y-%m-%d')

    
def convert_quantity(quantity_str):
    quantity_str = quantity_str.replace(',', '.')
    try:
        if '/' in quantity_str:
            quantity = float(Fraction(quantity_str))
        else:
            quantity = float(quantity_str)
        return str(quantity)
    except ValueError:
        return quantity_str