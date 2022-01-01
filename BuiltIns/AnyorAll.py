'''
Title     : Any or All
Subdomain : Built-Ins
Author: ThuongLe
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
'''
n = int(input())
ar = list(map(int,input().split()))
ar = sorted(ar)
if(ar[0]<=0):
    print(False)
else:
    chk = False
    for i in ar:
        s = str(i)
        if (s==s[::-1]):
            chk = True
            break
    print(chk)
