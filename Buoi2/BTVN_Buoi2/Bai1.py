thang = int(input("Tháng "))
nam = int (input("Năm "))

if thang < 1 or thang > 12:
    print("Tháng ko hợp lệ!")
elif thang == 2 and (nam % 400 == 0 or(nam % 4 == 0 and nam % 100 !=0)):
    print(29)
elif thang == 2:
    print(28)
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(30)
else:
    print(31)