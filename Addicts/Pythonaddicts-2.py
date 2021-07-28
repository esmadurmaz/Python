#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29,
       53, 54, 45, 19, 20, 47, 55, 39, 41, 7,
       9, 17, 26, 27, 42, 22, 37, 51, 46, 18,
       44, 30, 34, 13, 15, 35, 33, 16, 50, 24]

for i in range (6,55,2):
    if i not in num:
        print(i)


# In[10]:


row = int(input("Please enter you number : "))
 
for i in range (0, row+1, 1):
    print(" * " * i)
for i in range (row-1, 0, -1):
    print(" * " * i)


# In[ ]:




