import unittest
from src.PaymentData import PaymentData
from src.Flights import Flights
from src.Vol import Vol
from src.Hotel import Hotel
from src.Hotels import Hotels
from src.Car import Car
from src.Cars import Cars
from src.Viatgers import Viatgers

class test_calcula_preu_viatge(unittest.TestCase):

    def test_calcula_preu(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        f = Vol("1234ABC","MILAN", past, 10.0)
        f2 = Vol("5467DEF","PARIS", past, 20.0)
        Vtg=[f,f2]
        v = Flights(past, Vtg)
        c1 = Car("COTXE1","FERRARI","MILAN",4,30.0)
        cot=[c1]
        c = Cars(past,cot)
        h1 = Hotel("HOTEL1","MILANO",past,4,20.0)
        h2 = Hotel("HOTEL2", "LE PARIS", past, 6, 25.0)
        hot = [h1,h2]
        h = Hotels(hot)
        p=PaymentData("Visa", "Ruben", "1234", "1342", v, c, h)
        self.assertEqual(p.get_import_total(), 1160.0)

    def test_comprovacio_tipus_tarjeta_correcte(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        f = Vol("1234ABC", "MILAN", past, 10.0)
        f2 = Vol("5467DEF", "PARIS", past, 20.0)
        Vtg = [f, f2]
        v = Flights(past, Vtg)
        c1 = Car("COTXE1", "FERRARI", "MILAN", past, 30.0)
        cot = [c1]
        c = Cars(past, cot)
        h1 = Hotel("HOTEL1", "MILANO", past, 4, 20.0)
        h2 = Hotel("HOTEL2", "LE PARIS", past, 6, 25.0)
        hot = [h1, h2]
        h = Hotels(hot)
        p1=PaymentData("VISA","Samu","123456789","ABC",v, c, h)
        self.assertEqual(p1.comprobar_targeta(),True)

    def test_comprovacio_tipus_tarjeta_incorrecte(self):
        p = Viatgers(4)
        past = p.get_num_viatgers()
        f = Vol("1234ABC", "MILAN", past, 10.0)
        f2 = Vol("5467DEF", "PARIS", past, 20.0)
        Vtg = [f, f2]
        v = Flights(past, Vtg)
        c1 = Car("COTXE1", "FERRARI", "MILAN", past, 30.0)
        cot = [c1]
        c = Cars(past, cot)
        h1 = Hotel("HOTEL1", "MILANO", past, 4, 20.0)
        h2 = Hotel("HOTEL2", "LE PARIS", past, 6, 25.0)
        hot = [h1, h2]
        h = Hotels(hot)
        p2 = PaymentData("PAYPAL", "Samu", "123456789", "ABC", v, c, h)
        self.assertEqual(p2.comprobar_targeta(), False)

if __name__ == '__main__':
    unittest.main()
