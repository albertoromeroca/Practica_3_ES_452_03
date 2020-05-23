from . import Hotel

class Hotels:

    def __init__(self, llistahotels):
        self.llista_hotels = llistahotels
        pass

    def get_llista_vols(self):
        return self.llista_hotels
        pass

    def afegeix_hotel(self, hotel):
        self.llista_hotels.append(hotel)

    def elimina_hotel(self, nom_hotel):
        llista_nom_hotels = list()
        for i in self.llista_hotels:
            llista_nom_hotels.append(i.get_nom_hotel())
        if nom_hotel in llista_nom_hotels:
            index = 0
            trobat = False
            while trobat == False:
                if nom_hotel == llista_nom_hotels[index]:
                    trobat = True
                else:
                    index += 1
            self.llista_hotels.pop(index)
        else:
            return "Aquest hotel no existeix en el viatge!"

    def modifica_hotel(self, hotel_vell, hotel_nou):
        for index, valor in enumerate(self.llista_hotels):
            if valor == hotel_vell:
                self.llista_hotels[index] = hotel_nou

    def calcul_import_total_hotels(self):
        preu_final = 0.0
        for i in self.llista_hotels:
            preu_final += i.get_preu_hotel()
        return preu_final
