import unittest
from src.Viatgers import Viatgers


class gestionar_num_viatgers(unittest.TestCase):
    def test_get_num_viatgers(self):
        v = Viatgers(5)
        self.assertEqual(v.get_num_viatgers(), 5)

if __name__ == '__main__':
    unittest.main()