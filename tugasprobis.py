harga = int(input("harga: "))
jumlah = int(input(" jumlah: "))

total = harga * jumlah

if total > 250000:
    diskon = total * 0.4  # diskon 40%
else:
    diskon = 0

total_bayar = total - diskon

print("Total :", total)
print("Diskon:", diskon)
print("Total bayar:", total_bayar)