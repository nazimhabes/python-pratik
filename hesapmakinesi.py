def hesapmakinesi(isaret, sayi1, sayi2):
    if isaret == "+":
        return sayi1 + sayi2
    elif isaret == "-":
        return sayi1 - sayi2
    elif isaret == "*":
        return sayi1 * sayi2
    elif isaret == "/":
        return sayi1 / sayi2
    else:
        return "Hatalı işaret girdiniz!"

print(hesapmakinesi("*", 5, 6))