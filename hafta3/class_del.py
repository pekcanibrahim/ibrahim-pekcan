class sinif:
    metin =""

    def __init__(self, a):
        self.metin = a

    def __del__(self):
        print("beni destıroy ettiler")


nesne= sinif("Fatig Terim")

del nesne