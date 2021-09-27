def find_number(data):
    first = min(data)
    last = max(data)
    result = str()
    for i in range(first,last+1):
        if(not i in data):
            result+=(str(i)+", ")
    print("Lost numbers contain: ",result[0:-2])

num = [10, 11, 15, 12, 9, 14, 7]
find_number(num)
print()
num = [12, 5, 9, -3]
find_number(num)
