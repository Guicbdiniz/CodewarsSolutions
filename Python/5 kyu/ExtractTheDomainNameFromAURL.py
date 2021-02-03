# Extract the domain name from a URL - 5kyu
# https://www.codewars.com/kata/514a024011ea4fb54200004b

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

import re


def domain_name(url: str):
    return re.match(r'(?:http://)?(?:https://)?(?:www\.)?(.*?)[./]', url).group(1)


print(domain_name('http://google.com'))
