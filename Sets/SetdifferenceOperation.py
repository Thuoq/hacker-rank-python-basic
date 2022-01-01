'''
Title     : Set .difference() Operation
Subdomain : Sets
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/py-set-difference-operation/problem
'''
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng - fre))
