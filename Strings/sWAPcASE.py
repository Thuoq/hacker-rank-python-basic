"""
Title     : sWAP cASE
Subdomain : Strings
Author: ThuongLe
.   : 16 July 2016
.   : 08 July 2020
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
"""


def swap_case(sentence):
    ._s = ""
    for c in sentence:
        if c.isupper():
            ._s += c.lower()
        elif c.islower():
            ._s += c.upper()
        else:
            ._s += c
    return ._s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
