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

    for resident in data:
        if resident['country'] != "France":
            niss = "00000000000"
            keys_to_check = ['niss', 'social_security_number']
            for key in keys_to_check:
                nissTmp = resident.get(key)
                if nissTmp is not None:
                    nissTmp = re.sub(r'[\s\.\-]', '', nissTmp)
                    chiffres = re.findall(r'\d{11}', nissTmp)
                    if chiffres:
                        niss = chiffres[0]
                        break
            PATIENT = ET.SubElement(PATIENTS, 'PATIENT')
            ID = ET.SubElement(PATIENT, 'ID')
            ID.text = niss
            NAME = ET.SubElement(PATIENT, 'NAME')
            NAME.text = resident.get('lastname')
            FIRSTNAME = ET.SubElement(PATIENT, 'FIRSTNAME')
            FIRSTNAME.text = resident.get('firstname')
            LOCATION1 = ET.SubElement(PATIENT, 'LOCATION1')
            LOCATION1.text = resident.get('establishment')
            LOCATION2 = ET.SubElement(PATIENT, 'LOCATION2')
            LOCATION2.text = resident.get('establishment')
            BIRTHDATE = ET.SubElement(PATIENT, 'BIRTHDATE')
            BIRTHDATE.text = resident.get('birthdate')
            DOCTORNAME = ET.SubElement(PATIENT, 'DOCTORNAME') # If multiple presc who have diff doctor ?
            DOCTORNAME.text = resident.get('doctor_fullname')
            DOCTORMEDREGNR = ET.SubElement(PATIENT, 'DOCTORMEDREGNR')
            DOCTORMEDREGNR.text = resident.get('doctor_am_number')
            PATIENTUNIDOSE = ET.SubElement(PATIENT, 'PATIENTUNIDOSE')
            PATIENTUNIDOSE.text = "1"
            PRODUCTS = ET.SubElement(PATIENT, 'PRODUCTS')
            for medication in resident.get('medications'):
                PRODUCT = ET.SubElement(PRODUCTS, 'PRODUCT')
                PRODUCTID = ET.SubElement(PRODUCT, 'PRODUCTID')
                PRODUCTID.text = str(medication.get('cnk'))
                PRODUCTIDHOME = ET.SubElement(PRODUCT, 'PRODUCTIDHOME')
                SPECIALITY = ET.SubElement(PRODUCT, 'SPECIALITY')
                SPECIALITY.text = "1"
                DCS = ET.SubElement(PRODUCT, 'DCS')
                DCS.text = medication.get('name')
                TABLETUNIDOSE = ET.SubElement(PRODUCT, 'TABLETUNIDOSE')
                TABLETUNIDOSE.text = "1"
                ADMS = ET.SubElement(PRODUCT, 'ADMS')
                for date, details in medication.get('schedule'):
                    for posology in details
                        ADM = ET.SubElement(ADMS, 'ADM')
                        QTY = ET.SubElement(ADM, 'QTY')
                        QTY.text = posology.get('quantity') # .replace(",", ".") Only INT ?
                        ADMDATE = ET.SubElement(ADM, 'ADMDATE')
                        ADMDATE.text = date
                        ADMHOUR = ET.SubElement(ADM, 'ADMHOUR')
                        ADMHOUR.text = posology.get('time')
    tree = ET.ElementTree(root)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "00000554002_0000000000001234_"+now+"_TH"
    tree.write(filename+'.xml')