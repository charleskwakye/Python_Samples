import xml.etree. ElementTree as ET
xm1Doc = ET.parse("Files chapter 9/jobs.xml")
root = xm1Doc.getroot()
counter = 0
for company in root.find('jobs'):                           # For each company which are 3 in total
    company_name = company.find('name').text                # company name is the same for all vacancies in company
    contacts = company[1].find('email').text                # contact was only one per company
    vacancies = company[2]                                  # vacancies was the 3rd Sub-element of company
    for vacancy in vacancies:                               # for the number of vacancy in vacancies
        position = vacancy.find('position')                 # find the position per the vacancy
        if position.get('group') == 'IT':                   # if the position is IT
            counter += 1
            print(str(counter)+'.\tPosition:\t', position.text)
            print('\tCompany:\t',company_name)
            print('\tContact:\t',contacts, '\n')
