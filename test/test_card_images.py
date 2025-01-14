"""
File containing all tests for the CardImages class.

CardImages deals with the generation of the ASCII art for displaying cards in the terminal

"""
from src.card_images import CardImages
import unittest

SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


class CardImagesTestCase(unittest.TestCase):
    def setUp(self):
        self.card_images = CardImages()
        pass
    
    def tearDown(self):
        pass

    def test_get_image_by_name(self):
        """
        Given the card name is valid, the returned 
        """
        card_name = "2_of_Hearts"
        ascii_card = self.card_images.get_image_by_name(card_name)
        self.assertIsNotNone(ascii_card)
        self.assertIsInstance(ascii_card, list)
        self.assertEqual(len(ascii_card), 8)

    def test_get_image_by_name_invalid(self):
        card_name = "Invalid_Card"
        with self.assertRaises(ValueError):
            self.card_images.get_partial_image_by_name(card_name)

    def test_get_partial_image_by_name_valid(self):
        card_name = "2_of_Hearts"
        partial_image = self.card_images.get_partial_image_by_name(card_name)
        self.assertIsNotNone(partial_image)
        self.assertIsInstance(partial_image, list)
        self.assertEqual(len(partial_image), 8)
        for line in partial_image:
            self.assertEqual(len(line), 3)

    def test_get_partial_image_by_name_invalid(self):
        card_name = "Invalid_Card"
        with self.assertRaises(ValueError):
            self.card_images.get_partial_image_by_name(card_name)

    def test_get_all_cards(self):
        self.assertEqual(len(self.card_images._card_dict), 52)
        self.assertEqual(len(self.card_images._card_partial_dict), 52)

    def test_get_not_aces(self):
        self.card_images.get_not_aces()
        for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
            for suit in ["Diamonds", "Clubs", "Spades", "Hearts"]:
                card_name = f"{rank}_of_{suit}"
                self.assertIn(card_name, self.card_images._card_dict)
                self.assertIn(card_name, self.card_images._card_partial_dict)

    def test_get_aces(self):
        self.card_images.get_aces()
        for suit in ["Diamonds", "Clubs", "Spades", "Hearts"]:
            card_name = f"Ace_of_{suit}"
            self.assertIn(card_name, self.card_images._card_dict)
            self.assertIn(card_name, self.card_images._card_partial_dict)

