import unittest
from src.Skyscanner import Skyscanner
from unittest import mock


class Test_Confirmacio_reserva_vols(unittest.TestCase):

    @mock.patch('src.Skyscanner')
    def test_Confirmacio_reserva_vols(self, mock_skyscanner):
        self.assertTrue(mock_skyscanner.confirm_reserve())

    @mock.patch('src.Skyscanner')
    def test_Confirmacio_reserva_vols_error(self, mock_skyscanner):
        mock_skyscanner.confirm_reserve.return_value = False
        self.assertFalse(mock_skyscanner.confirm_reserve())


if __name__ == '__main__':
    unittest.main()
