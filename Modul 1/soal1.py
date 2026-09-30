buku = 3 * 25000
pulpen = 2 * 8000
flashdisk = 1 * 75000

total = buku + pulpen + flashdisk
diskon = total * 10 / 100
setelah_diskon = total - diskon
pajak = setelah_diskon * 11 / 100
total_bayar = setelah_diskon + pajak
kembalian = 200000 - total_bayar

print("Total harga buku =", buku)
print("Total harga pulpen =", pulpen)
print("Total harga flashdisk =", flashdisk)
print("Total sebelum diskon =", total)
print("Diskon =", diskon)
print("Harga setelah diskon =", setelah_diskon)
print("Pajak =", pajak)
print("Total pembayaran =", total_bayar)
print("Uang kembalian =", kembalian)