import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files chapter 9/measurements.xml")
root = xmlDoc.getroot()

measurement = ET.Element('measurement')
measurement.set('executor', 'CF')
number = ET.SubElement(measurement, 'number')
number.text = str(77)
month = ET.SubElement(measurement, 'month')
month.text = 'December'
location = ET.SubElement(measurement, 'location')
location.text = 'Block F'
root.append(measurement)
xmlDoc.write('more_measurements.xml')