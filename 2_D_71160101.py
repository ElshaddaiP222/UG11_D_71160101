def sisipKata() :
    cek = len(input1)
    hasil = input1[0:int(cek/2)] + input2 + input1[int(cek/2+0):]
    print (hasil.title())

input1 = str(input("Masukkan sebuah kata/kalimat : "))
input2 = str(input("Masukkan karakter yang ingin disisipkan : "))

sisipKata()