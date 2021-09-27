def color(data):
    result = {}
    data=data.split("-")
    for i in data:
        if(i in result):
            result[i]+=1
        else:
            result.setdefault(i,1)
    print(dict(sorted(result.items(),key=lambda x:x[0],reverse = True)))

sentence01 = "blue-green-red-red-blue-yellow-black-white-blue-red-green-black-black-blue"
sentence02 = "blue-blue-blue-blue-red-red-green-green-white-white"

color(sentence01)