var01 = {-100:"Alpha", 1:"Brovo", -5:"Charlie"}
var02 = {1.25:"Delta", -2.1:"Echo", 9:"Foxtrot"}

var01.update(var02)

var01 = dict(sorted(var01.items(),key=lambda x:x[0],reverse = True))
print(var01)

# result = dict()
# for i in  sorted(var01.keys(),reverse = True):
#     result[i] = var01[i]
# print(result)