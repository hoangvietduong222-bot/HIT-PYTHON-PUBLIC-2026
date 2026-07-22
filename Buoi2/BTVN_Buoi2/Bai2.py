ngay = int(input("Ngày "))
thang = int(input("Tháng "))

if thang < 1 or thang > 12 or (thang == 2 and ngay >= 30):
    print("Ngày hoặc tháng ko hợp lệ! ")

elif (21 <= ngay <= 31 and thang == 3) or (1 <= ngay <= 19 and thang == 4):
    print("Bạch Dương")
elif (20 <= ngay <= 30 and thang == 4) or (1 <= ngay <= 20 and thang == 5):
    print("Kim Ngưu")
elif (21 <= ngay <= 31 and thang == 5) or (1 <= ngay <= 20 and thang == 6):
    print("Song tử")
elif (21 <= ngay <= 30 and thang == 6) or (1 <= ngay <= 22 and thang == 7):
    print("Cự Giải")
elif (23 <= ngay <= 31 and thang == 7) or (1 <= ngay <= 22 and thang == 8):
    print("Sư Tử")
elif (23 <= ngay <= 31 and thang == 8) or (1 <= ngay <= 22 and thang == 9):
    print("Xử Nữ")
elif (23 <= ngay <= 30 and thang == 9) or (1 <= ngay <= 22 and thang == 10):
    print("Thiên Bình")
elif (23 <= ngay <= 31 and thang == 10) or (1 <= ngay <= 21 and thang == 11):
    print("Bọ Cạp")
elif (22 <= ngay <= 30 and thang == 11) or (1 <= ngay <= 21 and thang == 12):
    print("Nhân Mã")
elif (22 <= ngay <= 31 and thang == 12) or (1 <= ngay <= 19 and thang == 1):
    print("Ma Kết")
elif (20 <= ngay <= 31 and thang == 1) or (1 <= ngay <= 18 and thang == 2):
    print("Bảo Bình")
elif (19 <= ngay <= 29 and thang == 2) or (1 <= ngay <= 20 and thang == 3):
    print("Song Ngư")