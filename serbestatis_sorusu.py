import math

g = 9.8

h = float(input("Yuksekligi giriniz: "))
v0 = float(input("Baslangic hizini giriniz: "))

t = math.sqrt(2*h/g)
x = v0*t

vx = v0
vy = g*t
v = math.sqrt(vx**2 + vy**2)

print("Havada kalma suresi: %5.2f saniye" %t)
print("Yatayda alacagi yol: %5.2f metre" %x)
print("Yere çarpma hızı: %5.2f m/s" %v)