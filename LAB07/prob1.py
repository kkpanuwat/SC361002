minScr=maxScr=total=count=0
while True:
    number = int(input("Please Enter Number : "))
    if(number == 0):
        break
    if(count == 0):
        minScr = number
        maxScr = number
    if(number < minScr):
        minScr = number
    if(number > maxScr):
        maxScr = number
    total+=number
    count+=1
print("Min : ",minScr)
print("Max : ",maxScr)
print("Avrg : ",total/count)