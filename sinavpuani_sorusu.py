#İki vize ve bir final sınavına girilen üniversitede harf notuna vizeler 
#30 final ise %40 etkilidir. Bu üniversitenin harf ortalamasını hesaplayan kodu yazınız.
vize = input("vize girniz: ")
final = input("final giriniz: ") 
ortalama = int(vize)*(0.4) + int(final)*(0.6)

if(ortalama<10):
   print("FF KALDINIZ. ")
elif(ortalama<20): 
    print("FF KALDINIZ. ")
elif(ortalama<30): 
    print("DD KALDINIZ.")
elif(ortalama<40): 
    print("DC ÇALIŞMAN LAZIM ")
elif(ortalama<50):
   print("CC SINIR  ")
elif(ortalama<60):
    print("CB İYİ GİBİ ")
elif(ortalama<70): 
    print("BB GEÇERLİ ")
elif(ortalama<80):
    print("AB GEÇTİNN")
elif(ortalama<90): 
    print("AA VAYSS") 
elif(ortalama<100):
    print("AA GEÇTİN ZEKİ ŞEY")
