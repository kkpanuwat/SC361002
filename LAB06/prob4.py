result = list()
number  = int(input('Please Enter Number : '))
for i in range (1,number+1):
    if(i%2!=0):
        result.append(i)
print('odd in 1 -',number,'=',result)