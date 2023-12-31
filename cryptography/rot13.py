text = input()
SHIFT_AMOUNT = 13
ALPHABET_SIZE = 26


def rot13(target: str) -> str:
    """
    Rot13暗号
    13文字づつずらす
    """
    if 'a' <= target <= 'z':
        shifted_char = (ord(target) - ord('a') + SHIFT_AMOUNT) % ALPHABET_SIZE
        return chr(shifted_char + ord('a'))
    elif 'A' <= target <= 'Z':
        shifted_char = (ord(target) - ord('A') + SHIFT_AMOUNT) % ALPHABET_SIZE
        return chr(shifted_char + ord('A'))
    return target


result = ""
for char in text:
    result += rot13(char)
print(result)
