from itertools import permutations

# Kullanıcıdan alınan harfler
letters = input("Lütfen harfleri girin: ")

# Kombinasyonların kaç harfli olacağını sorgulayın
size = int(input("Kombinasyonlar kaç harfli olacak? "))

# Txt dosyası oluşturun ve yazma işlemini başlatın
with open('combinations.txt', 'w') as f:
  # Tüm kombinasyonları yazdırın
  for combination in permutations(letters, size):
    f.write(''.join(combination) + '\n')

print("Kombinasyonlar txt dosyasına yazıldı.")

with open('combinations.txt', 'r') as f:
  combinations = f.read().splitlines()

# Türkçe sözlük dosyasındaki kelimeleri oku
with open('combined.txt', 'r') as f:
  combined = f.read().splitlines()

# Türkçe olan kelimeleri bulun ve yeni txt dosyasına yazın
with open('turkish_combinations.txt', 'w') as f:
  for word in combinations:
    if word in combined:
      f.write(word + '\n')

print("Türkçe kelimeler txt dosyasına yazıldı.")