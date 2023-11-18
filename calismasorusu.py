
import sympy as sp6

def integral_hesapla():
    # Kullanıcıdan fonksiyonu ve aralığı alın
    fonksiyon = input("Integralini hesaplamak istediğiniz fonksiyonu girin: ")
    aralik = input("Integralin hesaplanacağı aralığı girin (örn: [a, b]): ")
    
    # Fonksiyonu sembolik ifadeye dönüştürün
    x = sp.symbols('x')
    f = sp.sympify(fonksiyon)
    
    # Integral hesaplama yöntemini seçin
    print("Integral hesaplama yöntemini seçin:")
    print("1. Riemann integrali")
    print("2. Simpson integrali")
    secim = input("Seçiminizi yapın (1 veya 2): ")
    
    # Integrali hesaplayın
    if secim == '1':
        integral = sp.integrate(f, (x, aralik[0], aralik[1]))
    elif secim == '2':
        integral = sp.integrate(f, (x, aralik[0], aralik[1]), method='simpson')
    else:
        print("Geçersiz seçim!")
        return
    
    # Sonucu ekrana yazdırın
    print("Integral sonucu:", integral)

integral_hesapla()
