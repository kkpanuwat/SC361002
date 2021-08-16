while True:
    number = int(input('Please Enter Number : '))
    result = "is prime number"
    if (number == 1):
        result = "is't prime number"
    for i in range(2,number):
        if number % i == 0:
            result = "is't prime number"
            break
    print(number,result)