#classe Prestito per gestire gli oggetti 'prestito'
class Prestito:
    def __init__(self, codP, data, id_strumento, cognome_allievo):
        self.codP = codP
        self.data = data
        self.id_strumenti = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f'{self.data} {self.id_strumenti} {self.cognome_allievo}'

    def __repr__(self):
        return str(self)