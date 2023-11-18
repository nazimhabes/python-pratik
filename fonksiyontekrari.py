import random

def mod(sayi, bolen):
    return sayi % bolen
    
for i in range(5):
    rastgelesayi = random.randint(1,100)
    rastgelebolen = random.randint(1,10)
    print("Sayı{}: {}, Bölen: {}, Kalan: {}".format(i+1, rastgelesayi, rastgelebolen, mod(rastgelesayi,rastgelebolen)))