#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
print(numbers[1:9:2])


# In[ ]:





# In[ ]:


num = int(input("Please enter you number : "))
isitprime  = True 
   
    if num == 1:
        isitprime = False
        
    for i in range (2,num):
        if (num % i == 0)
        isitprime = False
        break
    if isitprime:
        print("number is a prime.")
    else :
        print("number is not prime.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")


# In[ ]:


Given an N by N matrix, rotate it by 90 degrees clockwise. For example, given the following matrix:

[[1, 2, 3],

[4, 5, 6],

[7, 8, 9]]

you should return:

[[7, 4, 1],

[8, 5, 2],

[9, 6, 3]]


# In[ ]:


def rotate(a):
    return [list(i) for i in zip(*a[::-1])]


# In[ ]:





# In[ ]:


h_letters = []

for letter in 'human' :
    h_letters.append(letter)
    
print(h_letters)    


# In[ ]:




