while True:
    stdId = input("Please Enter Student ID : ")
    findIndex = stdId.find("-")
    print("Result",stdId[findIndex-1],"+",stdId[findIndex+1],"=",int(stdId[findIndex-1])+int(stdId[findIndex+1]))