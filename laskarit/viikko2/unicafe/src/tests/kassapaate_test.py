import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
 

class TestKassapaate(unittest.TestCase):

    
    def setUp(self):
        self.kassapaate = Kassapaate()


    def test_luotu_kasspaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)


    def test_alkusaldot_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_edullisen_osto_kateisella_oikein(self):
        takaisin = Kassapaate.syo_edullisesti_kateisella(self.kassapaate, 200)
        self.assertEqual(takaisin, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

        takaisin = Kassapaate.syo_edullisesti_kateisella(self.kassapaate, 250)
        self.assertEqual(takaisin, 10)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)


    def test_maukkaan_osto_kateisella_oikein(self):
        takaisin = Kassapaate.syo_maukkaasti_kateisella(self.kassapaate, 340)
        self.assertEqual(takaisin, 340)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
       
        takaisin = Kassapaate.syo_maukkaasti_kateisella(self.kassapaate, 1000)
        self.assertEqual(takaisin, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)


    def test_edullisen_osto_kortilla_oikein(self):
        maksukortti = Maksukortti(200)
        osto = Kassapaate.syo_edullisesti_kortilla(self.kassapaate, maksukortti)
        self.assertFalse(osto)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

        maksukortti = Maksukortti(1000)
        osto = Kassapaate.syo_edullisesti_kortilla(self.kassapaate, maksukortti)
        self.assertTrue(osto)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_maukkaan_osto_kortilla_oikein(self):
        maksukortti = Maksukortti(300)
        osto = Kassapaate.syo_maukkaasti_kortilla(self.kassapaate, maksukortti)
        self.assertFalse(osto)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 3.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)

        maksukortti = Maksukortti(1000)
        osto = Kassapaate.syo_maukkaasti_kortilla(self.kassapaate, maksukortti)
        self.assertTrue(osto)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_kassan_rahamaaran_muuttumattomuus_korttiostoissa(self):
        maksukortti = Maksukortti(390)
        Kassapaate.syo_edullisesti_kortilla(self.kassapaate, maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        maksukortti = Maksukortti(500)
        Kassapaate.syo_maukkaasti_kortilla(self.kassapaate, maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    
    def test_kortille_lataus_oikein(self):
        maksukortti = Maksukortti(1000)
        Kassapaate.lataa_rahaa_kortille(self.kassapaate, maksukortti, -500)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        maksukortti = Maksukortti(1000)
        Kassapaate.lataa_rahaa_kortille(self.kassapaate, maksukortti, 550)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 15.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100550)


