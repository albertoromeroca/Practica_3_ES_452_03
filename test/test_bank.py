import unittest
from src.Bank import Bank
from unittest import mock


class Test_Confirmacio_pagament(unittest.TestCase):

    @mock.patch('src.Bank')
    def test_Confirmacio_pagament(self, mock_bank):
        self.assertTrue(mock_bank.do_payment())

    @mock.patch('src.Bank')
    def test_Confirmacio_pagament_error(self, mock_bank):
        mock_bank.do_payment.return_value = False
        self.assertFalse(mock_bank.do_payment())


if __name__ == '__main__':
    unittest.main()