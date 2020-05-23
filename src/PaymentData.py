from . import Flights
from . import Hotels
from . import Cars

class PaymentData:

    def __init__(self, tipus, nom, num, codi, Vols, Cotxes, Hotels):
        self.tipus_targeta = tipus
        self.nom_titular = nom
        self.numero_targeta = num
        self.codi_seguretat = codi

        import_cars = 0
        if Cotxes:
            import_cars = Cotxes.calcul_import_total_cotxe()

        import_hotels = 0
        if Hotels:
            import_hotels = Hotels.calcul_import_total_hotels()

        self.import_total = Vols.calcul_import_total_vols()+import_cars+import_hotels
        pass

    def get_tipus_targeta(self):
        return self.tipus_targeta
        pass

    def get_nom_titular(self):
        return self.nom_titular
        pass

    def get_num_targeta(self):
        return self.numero_targeta
        pass

    def get_codi_seguretat(self):
        return self.codi_seguretat
        pass

    def get_import_total(self):
        return self.import_total
        pass

    def comprobar_targeta(self):
        if self.tipus_targeta == "VISA" or self.tipus_targeta == "MASTERCARD":
            return True
        else:
            return False