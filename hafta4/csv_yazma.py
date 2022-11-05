import csv

baslik = ["sicaklik", "nem", "basinc"]
veri = [[30, 75.6, 10], [33.2, 41.7, 36]]

with open ('sensor_veri.csv', 'w', encoding="UTF8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
