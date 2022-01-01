'''
Title     : Set .symmetric_difference() Operation
Subdomain : Sets
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
'''
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))
