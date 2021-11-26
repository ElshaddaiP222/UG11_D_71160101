def cekString():
    if m.isdigit and m % 2 == 0:
        print(" ", m/2)
    elif m.isdigit and m % 2 == 1:
        print(" ", m+5/2) 
    else: print(" ",m.reversed())


m = str(input("Masukan string : "))
cekString()

