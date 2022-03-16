import matplotlib.pyplot as plt
import numpy as np
import random
city_name=[]
data_p=[]
with open('city_population.txt') as file:
    line1=file.readline()
    line=file.readline().rstrip()
    record = line.split('#')
    while line:
        city_name.append(record[0])
        data_p.append(int(record[1]))
        line=file.readline().rstrip()
        record=line.split('#')
data = np.array(data_p,int)
total = data.sum()
plt.pie(data_p,labels=city_name,autopct='%1.1f%%',startangle=-40)
circle=plt.Circle((0,0),0.7,color='white')
p=plt.gcf()
p.gca().add_artist(circle)
plt.title('Population per city\n'+str(total))
plt.show()