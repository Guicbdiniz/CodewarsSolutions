# Extract the domain name from a URL - 5kyu

import re


def domain_name(url: str):
    return re.match(r'(?:http://)?(?:https://)?(?:www\.)?(.*?)[./]', url).group(1)


print(domain_name('http://google.com'))
