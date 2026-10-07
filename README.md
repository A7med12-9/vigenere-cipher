# Vigenere Cipher

[![tests](https://github.com/A7med12-9/vigenere-cipher/actions/workflows/tests.yml/badge.svg)](https://github.com/A7med12-9/vigenere-cipher/actions/workflows/tests.yml)

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

## Installation

There are three ways to get the project. Pick whichever you prefer.

### Option 1: Clone with Git (recommended)

```bash
git clone https://github.com/A7med12-9/vigenere-cipher.git
cd vigenere-cipher
```

### Option 2: Download as a ZIP

1. Open the [repository page](https://github.com/A7med12-9/vigenere-cipher).
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Extract the ZIP file, then open a terminal inside the extracted folder.

### Option 3: Download only the script

Since the program is a single file with no dependencies, you can grab just that:

```bash
curl -O https://raw.githubusercontent.com/A7med12-9/vigenere-cipher/main/vigenere_cipher_app.py
```

Or with `wget`:

```bash
wget https://raw.githubusercontent.com/A7med12-9/vigenere-cipher/main/vigenere_cipher_app.py
```

After downloading, check that Python 3 is installed:

```bash
python3 --version
```

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
