import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)



    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")
