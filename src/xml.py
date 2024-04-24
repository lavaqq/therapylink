import xml.etree.ElementTree as ET
import re
from datetime import datetime
import src.utils as utils

def create(data, sendernr, sendername, receivernr, receivername, start_date, end_date):
    root = ET.Element('THERAPIE')
    ET.SubElement(root, 'SENDERNR').text = sendernr
    ET.SubElement(root, 'SENDERNAME').text = sendername
    ET.SubElement(root, 'RECEIVERNR').text = receivernr
    ET.SubElement(root, 'RECEIVERNAME').text = receivername
    ET.SubElement(root, 'CREATIONDATETIME').text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    ET.SubElement(root, 'STARTDATE').text = start_date
    ET.SubElement(root, 'ENDDATE').text = end_date
    patients = ET.SubElement(root, 'PATIENTS')

    for resident in data:
        if rresident.get('country', '') == "Belgique":
            niss = "00000000000"
            keys_to_check = ['niss', 'social_security_number']
            for key in keys_to_check:
                niss_tmp = resident.get(key)
                if niss_tmp is not None:
                    niss_tmp = re.sub(r'[\s\.\-]', '', niss_tmp)
                    found = re.findall(r'\d{11}', niss_tmp)
                    if found:
                        niss = found[0]
                        break
            patient = ET.SubElement(patients, 'PATIENT')
            ET.SubElement(patient, 'ID').text = niss
            ET.SubElement(patient, 'NAME').text = resident.get('lastname', '')
            ET.SubElement(patient, 'FIRSTNAME').text = resident.get('firstname', '')
            ET.SubElement(patient, 'LOCATION1').text = resident.get('establishment', '')
            ET.SubElement(patient, 'LOCATION2').text = resident.get('establishment', '')
            ET.SubElement(patient, 'BIRTHDATE').text = resident.get('birthdate', '')
            ET.SubElement(patient, 'DOCTORNAME').text = resident.get('doctor_fullname', '')
            ET.SubElement(patient, 'DOCTORMEDREGNR').text = resident.get('doctor_am_number', '')
            ET.SubElement(patient, 'PATIENTUNIDOSE').text = "1"
            products = ET.SubElement(patient, 'PRODUCTS')

            for medication_id, medication_details in resident['medications'].items():
                cnk = medication_details.get('cnk')
                if cnk is not None:
                    product = ET.SubElement(products, 'PRODUCT')
                    ET.SubElement(product, 'PRODUCTID').text = str(cnk)
                    ET.SubElement(product, 'PRODUCTIDHOME')
                    ET.SubElement(product, 'SPECIALITY').text = "1"
                    ET.SubElement(product, 'DCS').text = medication_details.get('name', '')
                    ET.SubElement(product, 'TABLETUNIDOSE').text = "1"
                    adms = ET.SubElement(product, 'ADMS')
                    for date, schedules in medication_details.get('schedule', {}).items():
                        for period, details in schedules.items():
                            adm = ET.SubElement(adms, 'ADM')
                            ET.SubElement(adm, 'ADMDATE').text = date
                            ET.SubElement(adm, 'QTY').text = utils.convert_quantity(details.get('quantity', ''))
                            ET.SubElement(adm, 'ADMHOUR').text = details.get('time', '')
                else:
                    pass
        else:
            pass

    tree = ET.ElementTree(root)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"00000554002_0000000000001234_{now}_TH"
    tree.write(filename + '.xml')

