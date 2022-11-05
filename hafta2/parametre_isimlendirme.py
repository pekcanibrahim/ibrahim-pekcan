def topla(*toplanacak, fazladan=0):
    toplam = 0
    for deger in toplanacak:
        toplam += deger + fazladan
    return toplam

print(topla(3, 4, 5 ,6 , 7, fazladan=2))
