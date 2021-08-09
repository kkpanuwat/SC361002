###
# 3.50-4.00 ดีมาก
# 3.00 - 3.50 ดี
# 2.50 - 3.00 ปานกลาง
# 2.00 - 2.50 พอใช้
# 1.50 - 2.00 ปรับปรุง  
# ###

grade = float(input('Please Enter Your Grade : '))
if grade > 3.50 <= 4.00 :
    print('ดีมาก')
elif grade > 3.00 <= 3.50 :
    print('ดี')
elif grade > 2.50 <= 3.00 :
    print('ปานกลาง')
elif grade > 2.00 <= 2.50 :
    print('พอใช้')
else :
    print('ปรับปรุง')
    
