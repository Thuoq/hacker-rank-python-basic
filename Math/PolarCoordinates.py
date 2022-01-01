'''
Title     : Polar Coordinates
Subdomain : Math
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem
'''
import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
