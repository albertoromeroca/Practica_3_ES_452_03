class Car:

    def __init__(self, codi_cotxe, marca, lloc_recollida, dies, preu):
        self.codi_cotxe=codi_cotxe
        self.marca_cotxe=marca
        self.lloc_recollida=lloc_recollida
        self.dies_reserva=dies
        self.preu_total = preu*self.dies_reserva
        pass

    def get_codi_cotxe(self):
        return self.codi_cotxe
        pass

    def get_marca_cotxe(self):
        return self.marca_cotxe
        pass

    def get_lloc_recollida(self):
        return self.lloc_recollida
        pass

    def get_dies_reserva(self):
        return self.dies_reserva
        pass

    def get_preu_total(self):
        return self.preu_total
        pass