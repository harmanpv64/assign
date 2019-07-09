#Assingment 8
'''
We represent time in a way that’s easy for us to understand. However, Python stores it in tuples.
These python tuples are made of nine numbers.
Index	Field	       Domain of Values
0	  Year (4 digit)	   Ex.- 1995
1	  Month	           1 to 12
2	  Day	               1 to 31
3	  Hour	           0 to 23
4	  Minute	           0 to 59
5	  Second	           0 to 61 (60/61 are leap seconds)
6	  Day of Week	       0 to 6 (Monday to Sunday)
7	  Day of Year	       1 to 366 (Julian day)
8	  DST     	        -1,0,1
'''
#Q2
from datetime import date
print(date.today())
print(date.fromtimestamp(3452435))
#Q3
import datetime
a="1970/02/07"
d=datetime.datetime.strptime(a,"%Y/%m/%d")
print(d.month)
#Q4
import datetime
a="1970/12/12"
d=datetime.datetime.strptime(a,"%Y/%m/%d")
print(d.day)
#Q5
import datetime
a="11/01/2021"
d=datetime.datetime.strptime(a,"%d/%m/%Y")
print(d.day)
#Q6 local
import time
print(time.localtime())
#Q7
import math
a = int(input("Enter number:"))
fact = math.factorial(a)
print(f"factorial= {fact}")
#Q8
import math
a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
print(math.gcd(a,b))
#Q9
import os
print(os.getcwd())
print(os.environ)
