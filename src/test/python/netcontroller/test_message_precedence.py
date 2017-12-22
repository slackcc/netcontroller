import unittest

from netcontroller.precedence.precedence_cceb import PrecedenceCCEB


class TestPrecedenceMethods(unittest.TestCase):

    def test_order(self):
        self.assertTrue(PrecedenceCCEB.FLASH_OVERRIDE > PrecedenceCCEB.FLASH)
        self.assertFalse(PrecedenceCCEB.FLASH_OVERRIDE < PrecedenceCCEB.FLASH)
        self.assertTrue(PrecedenceCCEB.FLASH < PrecedenceCCEB.FLASH_OVERRIDE)
        self.assertTrue(PrecedenceCCEB.FLASH >= PrecedenceCCEB.FLASH)
        self.assertTrue(PrecedenceCCEB.FLASH <= PrecedenceCCEB.FLASH)
        self.assertTrue(PrecedenceCCEB.FLASH >= PrecedenceCCEB.ROUTINE)
        self.assertFalse(PrecedenceCCEB.FLASH <= PrecedenceCCEB.ROUTINE)


if __name__ == '__main__':
    unittest.main()
