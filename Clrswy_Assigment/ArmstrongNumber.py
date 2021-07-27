#!/usr/bin/env python
# coding: utf-8

# In[1]:


# take input from the user
num = int(input("Enter a number: "))
power = len(str(num))
# initialize sum
sum = 0
# find the sum of the cube of each digit
# temp = num
while num > 0:
   digit = num % 10   
   sum += digit ** power
   num //= 10
# display the result
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")


# In[ ]:




