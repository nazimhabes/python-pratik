r1 = float(input("R1 direncini giriniz: "))
r2 = float(input("R2 direncini giriniz: "))
r3 = float(input("R3 direncini giriniz: "))
r4 = float(input("R4 direncini giriniz: "))

v = float(input("Kaynaktaki gerilimi giriniz: "))

i = v/(r1+r2+r3+r4)
vr1 = i*r1
pr2 = i**2*r2

print("I: %5.2f A" %i)
print("VR1: %5.2f V" %vr1)
print("PR2: %5.2f W" %pr2)