# PR


# ---------5++++++9--------12+++++30----------
MasukanUser = int(input("masukan bilangan 5 sampai 9 dan lebih dari 12 sampai 30 : "))

print(MasukanUser)



# Cek Lebih Dari 5
lebDar = (MasukanUser >= 5)

print ("Lebih dari 5 : ", lebDar)

#Cek kurang Dari 9
kurDar = (MasukanUser <= 9)

print ("Kurang dari 9 : ", kurDar)

#Cek Lebih Dari 12
lebhDar = (MasukanUser >= 12)
print ("Lebih dari 12 : ", lebhDar)

#Cek Kurang Dari 30 
kurnDar = (MasukanUser <= 30)
print("kurang Dari 30 : ", kurnDar)

print("Maka kurang dari 5 itu Salah, Antara 5 sampai 9 itu benar, 10 dan 11 itu salah, antara 12 dan 30 itu benar, Lenih dari 30 itu Salah : ", kurDar and lebDar or lebhDar and kurnDar)
