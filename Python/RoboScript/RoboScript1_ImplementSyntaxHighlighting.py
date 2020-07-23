# RoboScript #1 - Implement Syntax Highlighting - 6 kyu


def highlight(code: str):
    highlighted_code = ''

    letter_to_color = {
        'F': 'pink',
        'L': 'red',
        'R': 'green'
    }

    for index, letter in enumerate(code):
        if letter in 'FLR':
            if index == 0 or code[index - 1] != letter:
                highlighted_code += '<span style="color: ' + letter_to_color[letter] + '">'

            highlighted_code += letter

            if index == len(code) - 1 or code[index + 1] != letter:
                highlighted_code += '</span>'

        elif letter in '0123456789':
            if index == 0 or code[index - 1] not in '0123456789':
                highlighted_code += '<span style="color: orange">'

            highlighted_code += letter

            if index == len(code) - 1 or code[index + 1] not in '0123456789':
                highlighted_code += '</span>'

        else:
            highlighted_code += letter

    return highlighted_code


print(highlight('FFFR345F2LL'))
