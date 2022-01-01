'''
Title     : Calendar Module
Subdomain : Date and Time
Author: ThuongLe

Problem   : https://www.hackerrank.com/challenges/calendar-module/problem
'''
import datetime
import calendar
m,d,y=map(int,input().split())
input_date = datetime.date(y,m,d)
print(calendar.day_name[input_date.weekday()].upper())
