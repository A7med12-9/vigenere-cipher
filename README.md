# Vigenere Cipher

A command-line Vigenere cipher tool written in Python. It encrypts and decrypts text, preserves upper/lower case, and leaves spaces and punctuation untouched.

> **Disclaimer:** The Vigenere cipher is an educational cipher that has been breakable since the 19th century (Kasiski examination, index of coincidence). This project is for learning and CTF practice. Do not use it to protect real data.

## Features

- Encrypt and decrypt with any letters-only keyword
- Preserves letter case
- Supports both conventions: classic (encrypt by adding the key) and reversed / Variant Beaufort (encrypt by subtracting the key)
- Input validation for the keyword and yes/no questions
- Unit tests for the core function

## Requirements

Python 3 (standard library only, no extra packages)

## Usage

```bash
python3 vigenere_cipher_app.py
```

The program asks for the text, the keyword, and whether to decrypt and/or use subtract mode, then prints the result. It keeps asking until you answer `n` to "Another one?".

## Examples

Classic mode, encrypting:

```
Text: ATTACK AT DAWN
Keyword: lemon
Decrypt? (y = decrypt, n = encrypt): n
Subtract mode? (y = encrypt by subtracting, n = classic): n
LXFOPV EF RNHR
```

Decrypting a message that was encrypted by subtracting the key:

```
Text: Txm srom vkda gl lzlgzr qpdb?
Keyword: friends
Decrypt? (y = decrypt, n = encrypt): y
Subtract mode? (y = encrypt by subtracting, n = classic): y
You were able to decode this?
```

## How it works

Each letter is shifted by the matching letter of the keyword, and the keyword repeats over the text. The shift only advances on letters, so spaces and punctuation do not consume key characters.

| Mode | Encrypt | Decrypt |
|---|---|---|
| Classic | plain + key | cipher - key |
| Subtract | plain - key | cipher + key |

All arithmetic is done modulo 26.

## Running tests

```bash
python3 -m unittest -v
```

## License

MIT, see [LICENSE](LICENSE).
