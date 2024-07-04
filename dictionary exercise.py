import random
names = ['Harsh','Aadhi','karunesh','sam']
eng_marks={}
for name in names:
    eng_marks.update({name:random.randint(0,100)})
print(eng_marks)


2

import random
names=['Harsh','Aadhi','karunesh','sam']
lang_marks={name:random.randint(0,100) for name in names}
print(lang_marks)


3

import random
names=['Harsh','Aadhi','karunesh','sam']
eng_marks={name:random.randint(0,100) for name in names}
lang_marks={'Harsh': 100, 'Aadhi': 50, 'Karunesh': 90, 'Sam': 5}
actualmarks=[]

actualmarks.append(eng_marks)
actualmarks.append(lang_marks)
print(actualmarks)


4

eng_marks={'Harsh': 92, 'Aadhi': 40, 'Karunesh': 50, 'Sam': 25}
lang_marks={'Harsh': 100, 'Aadhi': 50, 'Karunesh': 90, 'Sam': 5}
actualmarks=[eng_marks,lang_marks]
totalmarks=[]

for  key in eng_marks.keys():
    total=eng_marks[key]+lang_marks[key]
    totalmarks.append(total)
print(totalmarks)

6

names = ['Harsh', 'Aadhi', 'Karunesh', 'Sam']
subjects = ['Eng', 'Lang']
eng_marks = {'Harsh': 99, 'Aadhi': 50, 'Karunesh': 15, 'Sam': 19}
lang_marks = {'Harsh': 21, 'Aadhi': 80, 'Karunesh': 120, 'Sam': 141}
totalmarks=[120,130,135,160]
list_of_name_sub_tot=[(name,subjects[0],subjects[1],'total')for name in names]
class_marks={}
for name,total in zip(names,totalmarks):
    class_marks[(name,subjects[0],subjects[1],'total')]=[eng_marks[name],lang_marks[name],total]

    print("ultimate class marks dictionary:")
    print(class_marks)

7


names = ['Harsh', 'Aadhi', 'Karunesh', 'Sam']
subjects = ['Eng', 'Lang']
eng_marks = {'Harsh': 99, 'Aadhi': 50, 'Karunesh': 15, 'Sam': 19}
lang_marks = {'Harsh': 21, 'Aadhi': 80, 'Karunesh': 120, 'Sam': 141}
totalMarks = [120, 130, 135, 160]
list_of_name_sub_tot = [(name, subjects[0], subjects[1], 'total') for name in names]

class_marks = {}
for name, total in zip(names, totalMarks):
    class_marks[(name, subjects[0], subjects[1], 'total')] = [eng_marks[name], lang_marks[name], total]

for key in class_marks:
    total = class_marks[key][2]
    if total > 120:
        feedback = "Kutty Pattas"
    elif total > 100:
        feedback = "Good student"
    else:
        feedback = "Slow bloomer"
    class_marks[key].append(feedback)

print("Ultimate class marks dictionary with feedback:")
print(class_marks)
