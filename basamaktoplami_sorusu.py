sayi = input("sayı: ")
if int(sayi) < 10000 or int(sayi) > 99999:
    print("hata")
else:
    basamak1=int(sayi[0])
    basamak2=int(sayi[1])
    basamak3=int(sayi[2])
    basamak4=int(sayi[3])
    basamak5=int(sayi[4])

    deger=basamak1+basamak2+basamak3+basamak4+basamak5

    print(deger)