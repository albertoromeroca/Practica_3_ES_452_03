from . import Car

class Cars:

    def __init__(self,num_pasatgers, cotxe):
        if not num_pasatgers > 4:
            self.llista_cotxes = []
            for i in cotxe:
                self.llista_cotxes.append(i)
        pass

    def get_llista_cotxes(self):
        return self.llista_cotxes
        pass

    def afegir_cotxe(self,cotxe):
        self.llista_cotxes.append(cotxe)
        pass

    def eliminar_cotxe(self,cotxe):
        for index, item in enumerate(self.llista_cotxes):
            if self.llista_cotxes[index] == cotxe:
                self.llista_cotxes.pop(index)
        else:
            return "Aquest cotxe no existeix!"
        pass

    def modificar_cotxe(self,antic_cotxe,nou_cotxe):
        for index, item in enumerate(self.llista_cotxes):
            if self.llista_cotxes[index] == antic_cotxe:
                self.llista_cotxes[index] = nou_cotxe
        pass

    def calcul_import_total_cotxe(self):
        total = 0.0
        for i in self.llista_cotxes:
            total += i.get_preu_total()
        return total
        pass
