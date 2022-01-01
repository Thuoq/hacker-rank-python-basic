'''
Title     : Group(), Groups() &amp; Groupdict()
Subdomain : Regex and Parsing
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/re-group-groups/problem
'''
import re
s = input()
res = re.search(r'([A-Za-z0-9])\1',s)
if res == None:
    print(-1)
else:
    print(res.group(1))
