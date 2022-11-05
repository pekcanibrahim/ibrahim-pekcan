def topla_ne_varsagit(*a): # *a istediğin kadar parametre yolla
    toplam = 0
    for deger in a:
        toplam +=deger
    return toplam

print(topla_ne_varsagit(123,3,2,1,5,12,3123,1,23,123,1,1))