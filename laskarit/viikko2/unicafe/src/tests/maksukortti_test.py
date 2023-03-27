import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_lisays_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")

    def test_rahan_ottaminen_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodikutsusta_true_jos_rahaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(1000))

    def test_metodikutsusta_false_jos_ei_rahaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1300))

        



