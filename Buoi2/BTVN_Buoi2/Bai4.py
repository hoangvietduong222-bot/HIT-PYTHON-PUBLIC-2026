tien = int(input("xu "))

mua = tien // 28
tong = mua
vo = mua
while vo >= 3:
    doi = vo // 3
    tong += doi
    vo = vo % 3 + doi
print("Số chat có thể mua: ", tong)
