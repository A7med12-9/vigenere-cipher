"""Unit tests for the Vigenere cipher."""

import unittest

from vigenere_cipher_app import vigenere


class TestVigenere(unittest.TestCase):
    def test_classic_encrypt(self):
        # Textbook example: ATTACKATDAWN with key LEMON
        result = vigenere("ATTACKATDAWN", "LEMON", decrypt=False, subtract=False)
        self.assertEqual(result, "LXFOPVEFRNHR")

    def test_classic_roundtrip_preserves_case_and_punctuation(self):
        cipher = vigenere("Attack at Dawn!", "lemon", decrypt=False, subtract=False)
        plain = vigenere(cipher, "lemon", decrypt=True, subtract=False)
        self.assertEqual(plain, "Attack at Dawn!")

    def test_subtract_mode_decrypt(self):
        # Message encrypted by subtracting the key, as in the README example
        cipher = "Txm srom vkda gl lzlgzr qpdb?"
        result = vigenere(cipher, "friends", decrypt=True, subtract=True)
        self.assertEqual(result, "You were able to decode this?")

    def test_key_advances_only_on_letters(self):
        # If spaces consumed key characters, these two results would differ
        spaced = vigenere("a b", "bc", decrypt=False, subtract=False)
        compact = vigenere("ab", "bc", decrypt=False, subtract=False)
        self.assertEqual(spaced.replace(" ", ""), compact)


if __name__ == "__main__":
    unittest.main()
