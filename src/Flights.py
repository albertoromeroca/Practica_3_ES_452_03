from . import Vol

class Flights:

    def __init__(self, num_viatgers, vols):
        self.n_viatgers = num_viatgers
        self.llista_vols = vols
        pass

    def get_num_viatgers(self):
        return self.n_viatgers
        pass

    def calcul_import_total_vols(self):
        total = 0.0
        for i in self.llista_vols:
            total += i.get_preu_total()
        return total
        pass

    def afegeix_desti(self, vol):
        self.llista_vols.append(vol)

    def elimina_desti(self, desti):
        for index, item in enumerate(self.llista_vols):
            if desti == item.get_destinacio():
                self.llista_vols.pop(index)
        else:
            return "Aquest desti no existeix en el viatge!"

    def modifica_desti(self, vol_vell, vol_nou):
        for index,valor in enumerate(self.llista_vols):
            if valor == vol_vell:
                self.llista_vols[index] = vol_nou

    def get_llista_vols(self):
        return self.llista_vols

    def get_llista_hotels(self):
        return self.llista_hotels

