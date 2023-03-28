import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")
