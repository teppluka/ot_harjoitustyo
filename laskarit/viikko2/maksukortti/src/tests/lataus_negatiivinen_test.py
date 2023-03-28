import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_negatiivinen_lataus(self):
        kortti = Maksukortti(100)
        kortti.lataa_rahaa(-100)

        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
