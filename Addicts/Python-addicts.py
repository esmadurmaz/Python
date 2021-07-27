#!/usr/bin/env python
# coding: utf-8

# In[ ]:


What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
Take two inputs from the user word and word list and then write code that will find all the anagrams of a word from a list. You should return a list of all the anagrams or an empty list if there are none. For example:
input1:'abba'
input2: ['aabb', 'abcd', 'bbaa', 'dada']) 
output: ['aabb', 'bbaa']
input1:'racer'
input2: ['crazer', 'carer', 'racar', 'caers', 'racer'])
output: ['carer', 'racer']
input1:'laser'
input2:['lazing', 'lazy',  'lacer'])
output:[]


# In[1]:


listt_1 = []
inp1 = input('Enter a word > ')
while True:
    inp2 = input("Enter a word for the word list or 'q' to quit > ")
    if inp2.lower() == 'q':
        break
    else:
        listt_1.append(inp2)
listt_2 = []
sonuc = True
for i in listt_1:
    if set(i) == set(inp1):
        for j in i:
            if i.count(j) != inp1.count(j):
                sonuc = False
        if sonuc:
            if i not in listt_2:
                listt_2.append(i)
print(listt_2)


# In[2]:


anagram=input("enter a word =")
anagram_list=[] 
result=[]
b=0
while True:
    a=input("enter a word list =  Q use to for Quit    ").lower()
    if a =="q":
        break
    else:
        anagram_list.append(a)
for i in anagram_list:
    if sorted(list(i)) == sorted(anagram):
        result.append(i)
print(result)


# In[ ]:




