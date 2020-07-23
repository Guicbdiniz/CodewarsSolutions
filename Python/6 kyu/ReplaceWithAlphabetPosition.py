# Replace With Alphabet Position - 6kyu


def alphabet_position(text: str):
    return ' '.join([str('-abcdefghijklmnopqrstuvwxyz'.find(x)) for x in text.lower() if x.isalpha()])
