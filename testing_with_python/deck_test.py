from deckTest import Deck, Card
import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts","A")
    
    def test_init(self):
        """Cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form 'value of suite'"""
        self.assertEqual(repr(self.card), "A of Hearts")

   
        