# -*- coding: utf-8 -*-
"""Sort 3 integers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OHrU8hPUX9p7aqx2QehSSfgdqQAjPAww
"""

#9. Sort 3 integers
#   Given three integers (given through user input), sort the numbers using |min| and |max| functions.

a=int(input("Enter the number of a:"))
b=int(input("Enter the number of b:"))
c=int(input("Enter the number of c:"))
d=min(a,b,c)
e=max(a,b,c)
f=(a+b+c)-d-e
print("The Sorted order is:",d,f,e)

