weight = int(input('Enter your weight in kilograms: '))
length = int(input('Enter your length in centimetres: '))
bmi = (weight/(length*length))*10000
if bmi < 18:
    category = 'underwight'
elif  bmi <25:
    category = 'normal weight'
elif bmi <27:
    category = 'slightly overweight'
elif  bmi <30:
    category = 'moderate overweight'
elif bmi <40:
    category = 'obese'
elif 40>= bmi:
    category = 'sticky obese'

print('A person of',weight,'kg with a length of',length,'cm has as BMI',bmi,'\n This is a',category,)