import unittest

from netcontroller.communicators.address import Address


class TestAddressMethods(unittest.TestCase):
    street_address = "1 Main St"
    city = "Greenfield"
    state = "MA"
    zip_code = "01301"

    addr = Address(street_address,
                   city,
                   state,
                   zip_code)

    def test_init(self):
        self.assertEqual(self.addr.street_address, self.street_address)
        self.assertEqual(self.addr.city, self.city)
        self.assertEqual(self.addr.state, self.state)
        self.assertEqual(self.addr.zip_code, self.zip_code)

    def test_address(self):
        self.assertEqual(self.addr.address(), self.street_address + " " +
                         self.city + " " + self.state + " " + self.zip_code)


if __name__ == '__main__':
    unittest.main()
