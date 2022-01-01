'''
Title     : Detect Floating Point Numbers
Subdomain : Regex and Parsing
Domain    : Python


Problem   : https://www.hackerrank.com/challenges/introduction-to-regex/problem
'''

from re import match, compile

pattern = compile('^[-+]?\d*\.\d+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))
