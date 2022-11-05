"""
kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkarıp geri döndüren fonksiyonu yazın
"""
def pol_kontrol(*dram):
    toplam = fark = 0

    for sayi in dram:
        if str(sayi) == ''.join(reversed(str(sayi))):
            toplam += sayi
        else:
            fark += sayi
    return toplam - fark

print(pol_kontrol(10, 101, 55, 40, 9009))










