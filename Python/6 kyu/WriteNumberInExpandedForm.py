# Write Number in Expanded Form - 6 kyu
# https://www.codewars.com/kata/5842df8ccbd22792a4000245

# You will be given a number and you will need to return it as a string in Expanded Form.


def expanded_form(num):
    num_length = len(str(num))

    return ' + '.join([x[1].ljust(num_length - (x[0]), '0') for x in enumerate(str(num)) if x[1] != '0'])


print(expanded_form(1500))
