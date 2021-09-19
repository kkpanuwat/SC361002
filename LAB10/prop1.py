var01 = [1, 3, 5, 7, 9]
var02 = [2, 4, 6, 8, 10]
result = dict()

for i in range(3,25,1):
    if(i%3==0) :
        if(i%2==0):
            result[i] = var01.copy()
        else:
            result[i] = var02.copy()

print(result)