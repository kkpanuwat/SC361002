price = float(input("Please Enter Number: "))
if price > 100 :
    print('product:',price,'\nvat 7 % :',(price*7)/100,'\ntotal : ',price+((price*7)/100))
else :
    print('product:',price,'\ntotal : ',price)