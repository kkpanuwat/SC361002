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

if grade >= 3.25 <= 4.00 :
    getD = input('คุณเคยได้รับเกรด D หรือไม่\ny/Y = เคย\nn/N = ไม่เคย\n>>>')
    if getD == 'n' or getD == 'N' :
        if grade > 3.60 :
            print('ขอแสดงความยินดี คุณได้รับเกียรตินิยมอันดับที่ 1')
        else :
            print('ขอแสดงความยินดี คุณได้รับเกียรตินิยมอันดับที่ 2')
