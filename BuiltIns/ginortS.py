'''
Title     : ginortS
Subdomain : Built-Ins
Author: ThuongLe
Problem   : https://www.hackerrank.com/challenges/ginorts/problem
'''
s = input()
s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
print(*(s),sep = '')
