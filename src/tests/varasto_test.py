"""varasto-luokan testausta
"""
import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """varastoluokan testausluokka
    """
    def setUp(self):
        """luodaan testivarastot
        """
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-10, -2)
        self.varasto3 = Varasto(2,4)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """testataan tyhjän varaston luonti
        """
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """testataan uuden varaston oikea tilavuus
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """testataan saldon lisäys
        """
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """testataan että tavaran lisäys pienentää vapaata tilaa
        """
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """testataan että ottaminen antaa oikea määrän
        """
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """testataan että tavaran otta antaa lisää tilaa
        """
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_laitetaan_liikaa(self):
        """testataan että ei ylitäyty
        """
        self.varasto.lisaa_varastoon(12)
        #varastossa ei pitäisi olla tilaa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_liikaa(self):
        """testataan ettei anna liikaa
        """
        self.varasto.ota_varastosta(12)
        #varastossa ei pitäisi olla tilaa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_printtaustoimii(self):
        """testataan että tulostaa oikein
        """
        self.varasto.ota_varastosta(10)
        testistr = str(self.varasto)
        #saldon pitäisi olla 0, tilavuuden 10
        self.assertEqual(testistr, "saldo = 0.0, vielä tilaa 10.0")

    def test_ota_negatiivista(self):
        """testataan ettei voi ottaa negatiivista
        """
        self.varasto3.ota_varastosta(-2)
        #ei pitäisi vaikuttaa
        self.assertAlmostEqual(self.varasto3.paljonko_mahtuu(), 0)

    def test_ei_voi_luoda_negsaldo(self):
        """testataan ettei voi olla negatiivinen saldo
        """
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_ei_voi_luoda_negvol(self):
        """testataan ettei voi olla negatiivinen tilavuus
        """
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_ei_voi_luoda_liikaasaldoa(self):
        """testataan ettei saldo voi ylittää tilavuutta
        """
        self.assertAlmostEqual(self.varasto3.saldo, 2)

    def test_ei_lisata_neg(self):
        """testataan ettei voi lisätä negatiivista
        """
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
