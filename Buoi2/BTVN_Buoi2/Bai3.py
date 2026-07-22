n = int(input("Nhập n: "))

xoa = abs(n)
dem = 0
tong = 0

if xoa == 0:
    dem == 1
else: 
    while xoa > 0:
        dem += 1
        tong += xoa % 10
        xoa //= 10

if n<2:
    la_so_nguyen_to = False
else:
    la_so_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break

print("Số chữ số: ", dem)
print("Tổng chữ số: ", tong)

if la_so_nguyen_to:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
