import xml.etree.ElementTree as ET
from datetime import datetime

def create(data, sendernr, sendername, receivernr, receivername, start_date, end_date):
    root = ET.Element('THERAPIE')
    _SENDERNR = ET.SubElement(root, 'SENDERNR')
    _SENDERNAME = ET.SubElement(root, 'SENDERNAME')
    _RECEIVERNR = ET.SubElement(root, 'RECEIVERNR')
    _RECEIVERNAME = ET.SubElement(root, 'RECEIVERNAME')
    _CREATIONDATETIME = ET.SubElement(root, 'CREATIONDATETIME')
    _STARTDATE = ET.SubElement(root, 'STARTDATE')
    _ENDDATE = ET.SubElement(root, 'ENDDATE')
    _SENDERNR.text = sendernr
    _SENDERNAME.text = sendername
    _RECEIVERNR.text = receivernr
    _RECEIVERNAME.text = receivername
    _CREATIONDATETIME.text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    _STARTDATE.text = start_date
    _ENDDATE.text = end_date
    _PATIENTS = ET.SubElement(root, 'PATIENTS')