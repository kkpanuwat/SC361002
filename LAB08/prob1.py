result=str()
char = str()
while True:
    data = str(input("Please Enter Char : ")).upper()
    if(data == "Y"):
        break
    if(not data in char):
        char+=data
    result+=data
for i in char:
    print(i,"count : ",result.count(i))