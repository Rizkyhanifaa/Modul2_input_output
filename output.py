
#cetak string secara langsung
print("Halo, selamat pagi hari ini kita belajar python")
print("------------")

#cetak string menggunakan variabel
belajar = "Hallo, hari ini kita belajar Python"
print(belajar)
print("------------")

#cetak string menggunakan fungsi format
nama = "Hanifa"
print("Selamat Pagi {}".format(nama))
print("------------")


rida = "mie"
naya = "bakso"
caca = "sate"
print("Makanan Favorit Rida : " + str(rida)+ ", Makanan Favorit Naya : " +str(naya)+ ", Makanan Favorit Caca : " +str(caca) )
print("------------")

rida = "mie"
naya = "bakso"
caca = "sate"
print("Makanan Favorit Rida : {}\nMakanan Favorit Naya : {}\nMakanan Favorit Caca : {}\n".format(rida, naya, caca))
print("------------")


rida = "mie"
naya = "bakso"
caca = "sate"
print(f"Makanan Favorit Rida : {rida}\nMakanan Favorit Naya : {naya}\nMakanan Favorit Caca : {caca}\n")
print("------------")


panjang = 10
lebar = 5
luas = panjang * lebar
print("Luas = ", luas)

