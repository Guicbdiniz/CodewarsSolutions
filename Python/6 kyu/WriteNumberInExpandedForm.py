# Write Number in Expanded Form - 6 kyu
def expanded_form(num):
    num_length = len(str(num))

    return ' + '.join([x[1].ljust(num_length - (x[0]), '0') for x in enumerate(str(num)) if x[1] != '0'])


print(expanded_form(1500))
