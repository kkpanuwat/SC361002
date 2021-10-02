list01 = [-5, -7, 9, 14, 12]
list02 = [-3, -8, 10, 13, 17]

result = lambda x,check_list: x in check_list

str_result = ""
print('Intersection of the lists: ',end="")
for i in list01:
    if(result(i,list02)):
        str_result+=str(i)+", "
if(len(str_result)!=0):
    print(str_result[0:-2])
else:
    print("None")
