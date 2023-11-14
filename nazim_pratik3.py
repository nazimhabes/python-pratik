saat = int(input("Saat değerini giriniz: "))
dakika = int(input("Dakika değerini giriniz: "))

if saat > 12 or dakika > 60:
    print("Saat 12'den, dakika ise 60'tan büyük olamaz!")
else:
    saat_aci = saat * 30
    dakika_aci = dakika * 6
    aci = abs(saat_aci - dakika_aci)
    print("Saat ile dakika arasındaki açı:", aci)