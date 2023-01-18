import zipfile

# Zip dosyasını açın ve txt dosyalarını okuyun
with zipfile.ZipFile('zip.zip', 'r') as zip_ref:
  # Tüm txt dosyalarını okuyun
  txt_files = [f for f in zip_ref.namelist() if f.endswith('.txt')]
  contents = [zip_ref.read(f) for f in txt_files]

# Txt dosyalarının içeriklerini birleştirin
combined_contents = '\n'.join(content.decode() for content in contents)

# Birleştirilmiş içeriği yeni bir txt dosyasına yazın
with open('combined.txt', 'w') as f:
  f.write(combined_contents)

print("Txt dosyaları birleştirildi ve yeni dosyaya yazıldı.")