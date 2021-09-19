result = str()
data = str(input("Please Enter String : ")).upper()
for i in data:
    if(not i in result):
        result+=i
        print(i,"count : ",data.count(i))