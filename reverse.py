degisken = [1,2,3,4,5,6,7]
degisken_ters = []

#belli bir sayıda kodla döngü yapmak için range() fonksiyonu kullanılır. 
#range() fonksiyonu 3 parametre alır.
#range(başlangıç, bitiş, artış miktarı)
#başlangıç ve artış miktarı opsiyoneldir. 
#başlangıç verilmezse 0'dan başlar. 
#artış miktarı verilmezse 1 artar. 
#bitiş verilmezse sonsuza kadar devam eder.  
#range(5) 0'dan başlar 5'e kadar 1'er 1'er artar. 
#range(1,5) 1'den başlar 5'e kadar 1'er 1'er artar. 
#range(1,5,2) 1'den başlar 5'e kadar 2'şer 2'şer artar. 
#range(5,1,-1) 5'den başlar 1'e kadar 1'er 1'er azalır.

for i in range(len(degisken)):
    tersleme = degisken[abs(i-(len(degisken)-1))]
    degisken_ters.append(tersleme)

degisken.reverse()
    
print("manuel: ",degisken_ters)
print("reverse() kullanarak: ",degisken) 