import unittest
from src.Rentalcars import Rentalcars
from unittest import mock


class Test_Confirmacio_reserva_coches(unittest.TestCase):

    @mock.patch('src.Rentalcars')
    def test_Confirmacio_reserva_cotxe(self, mock_rentalcars):
        self.assertTrue(mock_rentalcars.confirm_reserve())
        mock_rentalcars.confirm_reserve.return_value = False
        self.assertFalse(mock_rentalcars.confirm_reserve())

    @mock.patch('src.Rentalcars')
    def test_Confirmacio_reserva_cotxe_error(self, mock_rentalcars):
        mock_rentalcars.confirm_reserve.return_value = False
        self.assertFalse(mock_rentalcars.confirm_reserve())


if __name__ == '__main__':
    unittest.main()
