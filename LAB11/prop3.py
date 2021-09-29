def color(data):
    result = {}
    data=data.split("-")
    for i in data:
        if(i in result):
            result[i]+=1
        else:
            result.setdefault(i,1)
    return (dict(sorted(result.items(),reverse = True)))

sentence01 = "blue-green-red-red-blue-yellow-black-white-blue-red-green-black-black-blue"
sentence02 = "blue-blue-blue-blue-red-red-green-green-white-white"

print(color(sentence01))