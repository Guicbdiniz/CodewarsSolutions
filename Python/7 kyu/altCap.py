# Alternate capitalization - 7kyu


def capitalize(s: str):
    first_string = ''
    second_string = ''

    for index in range(len(s)):
        if(index % 2 == 0):
            first_string += s[index].upper()
            second_string += s[index].lower()
        else:
            first_string += s[index].lower()
            second_string += s[index].upper()

    return [first_string, second_string]


if __name__ == "__main__":
    capitalize('oie')
