import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-10, -2)
        self.varasto3 = Varasto(2,4)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_laitetaan_liikaa(self):
        self.varasto.lisaa_varastoon(12)
        #varastossa ei pitäisi olla tilaa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_otetaan_liikaa(self):
        self.varasto.ota_varastosta(12)
        #varastossa ei pitäisi olla tilaa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_printtaustoimii(self):
        self.varasto.ota_varastosta(10)
        testistr = str(self.varasto)
        
        #saldon pitäisi olla 0, tilavuuden 10
        self.assertEqual(testistr, "saldo = 0.0, vielä tilaa 10.0")

    def test_ota_negatiivista(self):
        self.varasto3.ota_varastosta(-2)

        #ei pitäisi vaikuttaa
        self.assertAlmostEqual(self.varasto3.paljonko_mahtuu(), 0)

    def test_ei_voi_luoda_negsaldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_ei_voi_luoda_negvol(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_ei_voi_luoda_liikaasaldoa(self):
        self.assertAlmostEqual(self.varasto3.saldo, 2)

    def test_ei_lisata_neg(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
