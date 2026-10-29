penuh = 5

a = int(input("Masukkan jumlah penerima beasiswa penuh: "))
 
for i in range(a+1):
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    gaji = int(input("Penghasilan orang tua: "))
 
    if ipk < 3.00:
        print(nama, "-> Tidak memenuhi syarat")
        continue                     
 
    if gaji <= 3000000:
        print(nama, "-> Beasiswa penuh")
        penuh += 1 #menambah penerima beasiswa penuh
    elif gaji <= 5000000:
        print(nama, "-> Beasiswa sebagian")
    else:
        print(nama, "-> Tidak dapat beasiswa")
 
    if penuh == 3: #untuk memeriksa kuota penuh                    
        print("Kuota beasiswa penuh terpenuhi, seleksi dihentikan.")
        break