# studentnumber - r0879035
# family name and first name - Kwakye  Charles Nana
# class - 1 ACS 1

import xml.etree.ElementTree as ET
xmlDoc = ET.parse('grades.xml')
root = xmlDoc.getroot()

print('These courses are available:''\n')
counter = 0
for courses in root:
    for course in courses:
        counter += 1
        print(str(counter)+':',course.find('name').text)

user_input =input('\nPlease enter the number of a course: ')

if user_input == '1':
    print('The selected course is Application development in python')
if user_input == '2':
    print('The selected course is Data Analysis with SQL')


list_of_results = []
list_of_years = []
for course in root.find('course'):
    for score in course.find(score):
        score.append(list_of_results)

for year in root.find('year'):
    list_of_years.append(year.get('aj'))

averageresults = sum(list_of_results) / len(list_of_results)


import matplotlib.pyplot as plt
values = [9, 13, 3]
x=list_of_years
y=averageresults
plt.bar(list_of_years, y)
plt.subplot(132)
plt.xlabel('years')
plt.ylabel('Average_Results')
plt.suptitle('Categorical Plotting')
plt.title('Application Development in Python')
plt.plot(x, y)
plt.show()