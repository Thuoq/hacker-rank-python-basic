"""
Title     : Text Wrap
Subdomain : Strings
Author: ThuongLe

.   : 08 July 2020
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
