"""Vigenere cipher supporting both directions and mixed-case text."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def vigenere(text, keyword, decrypt, subtract):
    """Encrypt or decrypt text with a Vigenere keyword, preserving case.

    Classic convention: encrypt adds the key, decrypt subtracts it.
    subtract=True reverses this (Variant Beaufort).
    """
    # The key is subtracted when exactly one flag is set; both set cancel out.
    sign = -1 if (decrypt != subtract) else 1

    result = []
    keyword_index = 0

    for char in text:
        if char.lower() in ALPHABET:
            a = ALPHABET.find(char.lower())
            # Modulo makes a short keyword repeat over a longer text.
            b = ALPHABET.find(keyword[keyword_index % len(keyword)].lower())

            new_char = ALPHABET[(a + sign * b) % 26]
            result.append(new_char.upper() if char.isupper() else new_char)

            # Advance only on letters, otherwise spaces would consume key characters.
            keyword_index += 1
        else:
            result.append(char)

    return "".join(result)


def ask_yes_no(prompt):
    """Keep asking until the user answers y or n; return True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with y or n.")


def ask_keyword():
    """Keep asking until the keyword is letters only (find() fails silently otherwise)."""
    while True:
        keyword = input("Keyword: ").strip()
        if keyword.isalpha():
            return keyword
        print("Keyword must contain letters only, no spaces, digits or symbols.")


def main():
    while True:
        text = input("Text: ")
        keyword = ask_keyword()
        decrypt = ask_yes_no("Decrypt? (y = decrypt, n = encrypt): ")
        subtract = ask_yes_no("Subtract mode? (y = encrypt by subtracting, n = classic): ")

        print(vigenere(text, keyword, decrypt=decrypt, subtract=subtract))

        if not ask_yes_no("Another one? (y/n): "):
            break


if __name__ == "__main__":
    main()