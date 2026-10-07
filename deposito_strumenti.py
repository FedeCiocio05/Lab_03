import csv

import prestito
from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

        #lista contenente tutti gli oggetti
        self.lista_strumenti = []
        #lista prestiti
        self.lista_prestito = []
        self.num_prestiti = 0

        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=',')
                for row in reader:  # per ogni riga nel file
                    try:
                        # estraggo i singoli valori dalle colonne

                        codUnivoco = row[0]
                        tipo = row[1]
                        marca = row[2]
                        anno_acquisto = int(row[3])
                        valore = float(row[4])

                        # creo un oggetto Auto con i dati della riga
                        strumento = Strumento(codUnivoco, tipo, marca, anno_acquisto, valore)

                        # aggiungo l’auto alla lista
                        self.lista_strumenti.append(strumento)

                    except IndexError:
                        # errore se la riga ha meno colonne del previsto
                        print(f"Attenzione errore sugli indici,riga incompleta")  # gestione errore sugli indici
                    except ValueError:
                        # errore se i valori non sono convertibili nel formato corretto
                        print(f"Attenzione: riga contiene valori non validi")  # gestione errore sui valori
        except FileNotFoundError:
            # nel caso il file non esiste
            print(f"Errore: il file {file_path} non esiste.")
        except Exception:
            # altro errore non previsto
            print(f"Errore imprevisto")

        # restituisce comunque la lista aggiornata (anche se vuota)
        return self.lista_strumenti
        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        c = f'S{len(self.lista_strumenti)+1}'
        self.lista_strumenti.append(Strumento(c, tipo, marca, anno_acquisto, valore))
        return self.lista_strumenti
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.lista_strumenti, key=lambda s: s.marca)
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        #codice
        #se codS non presente o già in lista --> errore generico
        for s in self.lista_strumenti:
            if s.codunivoco == id_strumento:
                #vedere se strumento è già prestato
                for p in self.lista_prestito:
                    if id_strumento == p.id_strumento:
                        raise Exception("Lo strumento è già in prestito")

                self.num_prestiti += 1
                prestito = Prestito(f'P{self.num_prestiti}', data, id_strumento, cognome_allievo)
                self.lista_prestito.append(prestito)
                return prestito
        raise Exception("Lo strumento non è presente nel deposito")
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for p in self.lista_prestito:
            if id_prestito == p.codP:
                self.lista_prestito.remove(p)
                return self.lista_prestito
        raise Exception("Il prestito non esiste")
        # TODO
