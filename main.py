# 1-m
class Mahsulot:
    chegirma = 0

    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    def yakuniy_narx(self):
        return self.narx * (100 - self.chegirma) // 100

    @classmethod
    def chegirma_belgila(cls, foiz):
        cls.chegirma = foiz
        print(f"Barcha mahsulotlarga {foiz}% chegirma!")


a = Mahsulot("Telefon", 3000000)
b = Mahsulot("Quloqchin", 200000)
print(a.nom, a.yakuniy_narx())


Mahsulot.chegirma_belgila(20)
print(a.nom, a.yakuniy_narx())
print(b.nom, b.yakuniy_narx())


