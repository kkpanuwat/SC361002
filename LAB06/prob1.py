while True:
    score = float(input('Please Enter Score : '))
    if (score >= 80 and score <= 100):
        print('Grade : A')
    elif (score >= 75  and score < 80):
        print('Grade : B+')
    elif (score >= 70 and score < 75):
        print('Grade : B')
    elif (score >= 65 and score < 70):
        print('Grade : C+')
    elif (score >= 60 and score < 65):
        print('Grade : C')
    elif (score >= 55 and score < 60):
        print('Grade : D+')
    elif (score >= 50 and score < 55):
        print('Grade : D')
    elif (score >= 0  and score < 50):
        print('Grade : F')
    else:
        print('Please Enter Score Between 0-100')
