import unittest
from src.Vol import Vol
from src.Flights import Flights
from src.Car import Car
from src.Cars import Cars
from src.Hotel import Hotel
from src.Hotels import Hotels
from src.Viatgers import Viatgers

class test_gestionar_vols(unittest.TestCase):

    def test_buit_vol_llista_vols(self):
        vols = list()
        v = Flights(3, vols)
        test_llista_vols = list()
        self.assertEqual(v.get_llista_vols(), test_llista_vols)

    def test_buit_calcular_import(self):
        vols = list()
        v = Flights(3, vols)
        self.assertEqual(v.calcul_import_total_vols(), 0)

    def test_afegir_vol_llista_vols(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        f3 = Vol("CODIGO3", "PARIS", past, 32.0)
        vols = [f1, f2]
        v = Flights(past, vols)
        v.afegeix_desti(f3)
        test_llista_vols = [f1, f2, f3]
        self.assertEqual(v.get_llista_vols(), test_llista_vols)

    def test_afegir_vol_calcular_import(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        f3 = Vol("CODIGO3", "PARIS", past, 32.0)
        vols = [f1, f2]
        v = Flights(past, vols)
        v.afegeix_desti(f3)
        self.assertEqual(v.calcul_import_total_vols(), 228.0)

    def test_eliminar_vol_llista_hotels(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        vols = [f1, f2]
        v = Flights(past, vols)
        v.elimina_desti("BARCELONA")
        test_llista_vols = [f1]
        self.assertEqual(v.get_llista_vols(), test_llista_vols)

    def test_eliminar_vol_calcular_import(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        vols = [f1, f2]
        v = Flights(past, vols)
        v.elimina_desti("BARCELONA")
        self.assertEqual(v.calcul_import_total_vols(), 75.0)

    def test_modificar_vol_llista_hotels(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        vols = [f1]
        v = Flights(past, vols)
        v.modifica_desti(f1, f2)
        test_llista_vols = [f2]
        self.assertEqual(v.get_llista_vols(), test_llista_vols)

    def test_modificar_vol_calcular_import(self):
        p = Viatgers(3)
        past = p.get_num_viatgers()
        f1 = Vol("CODIGO1", "MILAN", past, 25.0)
        f2 = Vol("CODIGO2", "BARCELONA", past, 19.0)
        vols = [f1]
        v = Flights(past, vols)
        v.modifica_desti(f1, f2)
        self.assertEqual(v.calcul_import_total_vols(), 57.0)

class test_gestionar_cotxes(unittest.TestCase):

    def test_afegir_cotxe_import_total(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        c1 = Car("COTXE1","CITROEN", "LLOC1", past, 25.0)
        c2 = Car("COTXE2","SEAT", "LLOC2", past, 19.0)
        c3 = Car("COTXE3","MERCEDES-BENZ","LLOC3", past, 32.0)
        cotxes = [c1,c2]
        c = Cars(past,cotxes)
        c.afegir_cotxe(c3)
        self.assertEqual(c.calcul_import_total_cotxe(),304.0)

    def test_eliminar_cotxe_import_total(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        c1 = Car("COTXE1", "CITROEN", "LLOC1", past, 25.0)
        c2 = Car("COTXE2", "SEAT", "LLOC2", past, 19.0)
        cotxes = [c1,c2]
        c = Cars(past,cotxes)
        c.eliminar_cotxe(c2)
        self.assertEqual(c.calcul_import_total_cotxe(), 100.0)

    def test_modificar_cotxe_import_total(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        c1 = Car("COTXE1", "CITROEN", "LLOC1", past, 25.0)
        c2 = Car("COTXE2", "SEAT", "LLOC2", past, 19.0)
        cotxes = [c1]
        c = Cars(past,cotxes)
        c.modificar_cotxe(c1,c2)
        self.assertEqual(c.calcul_import_total_cotxe(), 76.0)

class test_gestionar_hotels(unittest.TestCase):

    def test_afegir_hotel_calcular_preu(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        h1 = Hotel("SVC_1", "ATENEA", past, 5, 23)
        h2 = Hotel("SVC_2", "IBIS", past, 7, 34)
        h3 = Hotel("SVC_3", "KINGH", past, 4, 15)
        hotels = [h1, h2]
        H = Hotels(hotels)
        H.afegeix_hotel(h3)
        test_preu = 1652.0
        self.assertEqual(H.calcul_import_total_hotels(), test_preu)

    def test_eliminar_hotel_calcular_preu(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        h1 = Hotel("SVC_1", "ATENEA", past, 5, 23)
        h2 = Hotel("SVC_2", "IBIS", past, 7, 34)
        h3 = Hotel("SVC_3", "KINGH", past, 4, 15)
        hotels = [h1, h2, h3]
        H = Hotels(hotels)
        H.elimina_hotel("KINGH")
        test_preu = 1412.0
        self.assertEqual(H.calcul_import_total_hotels(), test_preu)

    def test_modificar_hotel_calcular_preu(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        h1 = Hotel("SVC_1", "ATENEA", past, 5, 23)
        h2 = Hotel("SVC_2", "IBIS", past, 7, 34)
        hotels = [h1]
        H = Hotels(hotels)
        H.modifica_hotel(h1, h2)
        test_preu = 952.0
        self.assertEqual(H.calcul_import_total_hotels(), test_preu)


if __name__ == '__main__':
    unittest.main()
