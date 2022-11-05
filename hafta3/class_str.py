class sinif:
    metin =""

    def __init__(self, a):
        self.metin = a

    def __str__(self):
        return "yazdirilan : "+ self.metin


nesne= sinif("Fatig Terim")
print(nesne)
