dict_student = {"001":{"sex":"F","GPA":3.50},
"002":{"sex":"M","GPA":2.67},
"003":{"sex":"M","GPA":3.28},
"004":{"sex":"M","GPA":2.75},
"005":{"sex":"F","GPA":3.21},
"006":{"sex":"M","GPA":2.62},
"007":{"sex":"F","GPA":3.00},
"008":{"sex":"F","GPA":2.30}}
f = 0
m = 0
for i in dict_student:
    if(dict_student[i]['GPA']<3.00):
        if(dict_student[i]['sex']=='M'):
            m+=1
        else:
            f+=1
print('There are',(f+m),'students who have GPA less than 3.00\nFemale =',f,'\nMale =',m)
