def benim_fonk(n):
    return lambda a: a*n

katini_al = benim_fonk(2) #2 değeri n ye 5 değeri a ya atanır
print(katini_al(5))
katini_al = benim_fonk(5)
print(katini_al(5))

