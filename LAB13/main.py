def addStudent():
    file = open('./student.txt','a+',encoding='utf8')
    id = input("Enter Student Id : ")
    name = input("Enter Student Name : ")
    gpa = float(input("Enter Student Gpa : "))
    file.write(id+","+name+","+str(gpa)+",\n")
    file.close()

def showStudent():
    print("ID\t\t\tName\t\t\tGPA\n"+("="*50))
    gpa = 0
    count = 0
    file = open('./student.txt','r+',encoding="utf8")
    for i in file:
        i=i.split(',')[0:-1]
        print(i[0]+"\t\t\t"+i[1]+"\t\t\t"+i[2])
        gpa += float(i[2])
        count += 1
    print("Average of GPA is : ",(gpa/count))
    file.close()

def searchStudent():
    id = input("Student Id : ")
    file = open('./student.txt','r',encoding="utf8")
    result  = "Student not found."
    for i in file:
        i=i.split(',')[0:-1]
        if(i[0] == id):
            result="Student Id : "+i[0]+"\nStudent Name : "+i[1]+"\nStudent GPA : "+i[2]
    print(result)



while True:
    menu = int(input('=== SELECT MENU ===\n1.Add Student Data\n2.Show Student Data\n3.Search Student Data\n4.Exit\nSelect menu number [1-4] : '))
    if(menu == 1):
        addStudent()
    if(menu == 2):
        showStudent()
    if(menu == 3):
        searchStudent()
    if(menu == 4):
        break
