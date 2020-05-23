class Vol:

    def __init__(self, codi_vol,dest,num_past, preu_persona):
        self.codi_vol=codi_vol
        self.destinacio=dest
        self.n_passatgers=num_past
        self.preu_persona = preu_persona
        self.preu_total = preu_persona*self.n_passatgers
        pass

    def get_codi_vol(self):
        return self.codi_vol
        pass

    def get_destinacio(self):
        return self.destinacio
        pass

    def get_num_passatgers(self):
        return self.n_passatgers
        pass

    def get_preu_persona(self):
        return self.preu_persona
        pass

    def get_preu_total(self):
        return self.preu_total
        pass