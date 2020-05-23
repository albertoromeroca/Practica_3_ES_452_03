class Hotel:

    def __init__(self,codi,nom,numero_hostes,dies,preu_diari_persona):
        self.codi_hotel=codi
        self.nom_hotels=nom
        self.num_hotes=numero_hostes
        hab = numero_hostes/3
        if (numero_hostes%3)!=0:
            hab += 1
        self.num_habitacions= hab
        self.dies_reserva=dies
        self.preu_total = preu_diari_persona * self.dies_reserva * self.num_hotes
        pass

    def get_codi_hotel(self):
        return self.codi_hotel
        pass

    def get_nom_hotel(self):
        return self.nom_hotels
        pass

    def get_num_hotes(self):
        return self.num_hotes
        pass

    def get_num_habitacions(self):
        return self.num_habitacions
        pass

    def get_dies_reserva(self):
        return self.dies_reserva
        pass

    def get_preu_hotel(self):
        return self.preu_total