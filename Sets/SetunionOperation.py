'''
Title     : Set .union() Operation
Subdomain : Sets
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/py-set-union/problem
'''
n = input()
eng = set(map(int,input().split()))
b = input()
fre = set(map(int,input().split()))
print(len(eng.union(fre)))
