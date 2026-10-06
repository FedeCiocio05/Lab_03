class Strumento:
    def __init__(self, codUnivoco, tipo, marca, anno_acquisto, valore):
        self.codUnivoco = codUnivoco
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f'{self.codUnivoco} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore}'

    def __repr__(self):
        return str(self)