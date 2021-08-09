###GRADE
# A > 80
# B+ > 75
# B > 70
# C+ > 65
# C > 60
# D+ > 55
# D > 50
# F < 50
# ###

score = float(input('Please Enter Score: '))
if(score >= 80):
    print('A')
elif(score>=75):
    print('B+')
elif(score>=70):
    print('B')
elif(score>=65):
    print('C+')
elif(score>=60):
    print('C')
elif(score>=55):
    print('D+')
elif(score>=50):
    print('D')
else:
    print('F')