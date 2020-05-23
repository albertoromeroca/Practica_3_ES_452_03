import unittest
from src.Booking import Booking
from unittest import mock

class Test_Confirmacio_reserva(unittest.TestCase):

    @mock.patch('src.Booking')
    def test_Confirmacio_reserva_hotel(self, mock_booking):
        self.assertTrue(mock_booking.confirm_reserve())

    @mock.patch('src.Booking')
    def test_Confirmacio_reserva_hotel_error(self, mock_booking):
        mock_booking.confirm_reserve.return_value = False
        self.assertFalse(mock_booking.confirm_reserve())

if __name__ == '__main__':
    unittest.main()
