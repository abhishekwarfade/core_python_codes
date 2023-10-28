#!/usr/bin/env python
# coding: utf-8

# In[1]:


#traversing set
#only for loop for traversing of element
a={10,20,30}
for x in a:
    print(x,type(x))


# In[2]:


#basic set operation:
#union (|) 
a={10,20,30}
b={30,40,50}
a | b


# In[3]:


#intersection operator(&)
a={10,20,30}
b={30,40,50}
a & b


# In[4]:


#difference(-)
a={10,20,30}
b={30,40,50}
a - b


# In[5]:


b-a


# In[12]:


#symmetric diffrence  every elemnt from both set except common element 
a={10,20,30}
b={30,40,50}
a ^ b


# In[13]:


a.symmetric_difference_update(b)
a


# In[14]:


#membership operator
a={10,20,30}
10 in a


# In[15]:


10 not in a


# In[16]:


#relational operator
a={10,20,30}
b={30,40,50}
a==b


# In[17]:


a={10,20,30}
b={30,40,50}
a!=b


# In[18]:


a={10,20,30}
b={30,40,50}
a>b


# In[19]:


a={10,20,30}
b={30,40,50}
a<b


# In[20]:


a={10,20,30}
b={30,40,50}
a>=b


# In[21]:


a={10,20,30}
b={30,40,50}
a<=b


# In[23]:


a={x for x in range(5)}
a


# In[24]:


a=set()
for x in range(5):
    a.add(x)
print(a)    


# In[ ]:





# In[28]:


#wap to create set of charactes from a to z
a=set()
for x in range(65,91):
    a.add(chr(x))
print(a)
print(sorted(a))
len(a)


# In[33]:


a={chr(x) for x in range (ord("A"),ord("Z")+1)}
a


# In[34]:


#wap to accept set as input and print element in descending order
a=eval(input("enter set in {}")) #ascending by default
print(sorted(a))


# In[36]:


a=eval(input("enter set in {}")) #descending
print(sorted(a,reverse=True))


# In[37]:


a=eval(input("enter set in {}")) #descending
print(sorted(a,reverse=True))
for x in sorted(a):
    print(x,end="\t")


# In[42]:


s={int(x) for x in input().split()}

for x in sorted(s,reverse=True):
    print(x,end="\t")


# In[43]:


#wap to read a string and create set of unique characters in it.
string=input("enter the string")
s=set(string)
print("set of unique cxharacters",s)


# In[44]:


#wap to find common characters in two string
string1=input("enter the string")
string2=input("enter the string")
print("set of common characters",set(string1) & set(string2))


# In[45]:


#wap to read two string and print charac ters that are in A but not in B
string1=input("enter the string")
string2=input("enter the string")
print("set of common characters",set(string1) - set(string2))


# In[49]:


#WAP TO READ TWO STRINGS AND CHECK IF ALL CHARACTERS OF STRING1 APPEAR INSTRING 2 at least once
string1=input("enter the string")
string2=input("enter the string")
print(set(string1).issubset(set(string2)))


# In[47]:


string1=input("enter the string")
string2=input("enter the string")
if set(string1) <=set(string2):
    
    print("all characters appears in string 2")
else:
    print("all characters not appears in string 2")


# In[50]:


#wap to read two strings and check if both contains same characters (oredr does not match)

string1=input("enter the string")
string2=input("enter the string")
if set(string1) ==set(string2):
    
    print("identicle sets ")
else:
    print("not identicle sets ")


# In[54]:


a={chr(x) for x in range (ord("A"),ord("Z")+1)}
string1=input("enter the string")
if a== set(string1):
    print("string contain all the characters from a to z")
else: 
    print("string does not contain  characters from a to z")


# In[1]:


import string
a=set(string.ascii_uppercase)
string1=input("enter the string")
if a== set(string1):
    print("string contain all the characters from a to z")
else: 
    print("string does not contain  characters from a to z")


# In[57]:


a={10,20,30,40,50}
b={30,40,50}
a>b


# In[60]:


a={30,40,50}
b={30,40,50}
a>=b


# In[64]:


b={30,40,50}
a={30,40,50}
a<b


# In[63]:


b={10,20,30,40,50}
a={30,40,50}
a<=b


# In[ ]:




