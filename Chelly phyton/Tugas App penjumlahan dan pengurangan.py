#Tugas App Penjumlahan dan pengurangan

MasukanRumus = input ("Penjumlahan/pengurangan : " )

if MasukanRumus == "penjumlahan1" :
    print("anda memasuki program penjumlahan")
    MasukanNilai1= int(input("Nilai :"))
    MasukanNilai2 = int(input("Nilai :"))
    hasil = (MasukanNilai1 + MasukanNilai2)
    print("Hasil =", hasil)
elif MasukanRumus == "pengurangan2" :
    print("anda memasuki program pengurangan2")
    MasukanNilai1= int(input("Nilai :"))
    MasukanNilai2 = int(input ("Nilai :"))
    hasil = MasukanNilai1 - MasukanNilai2
    print("Hasil = ", hasil)
else :
    print ("Rumus Tidak Sesuai")
    print ("Program Selesai")