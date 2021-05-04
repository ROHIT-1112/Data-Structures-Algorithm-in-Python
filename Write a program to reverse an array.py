#!/usr/bin/env python
# coding: utf-8

# In[41]:


ary =[11,19,10,188,1887,253]
for index,value in enumerate(ary):
    print(index,value)


# In[42]:


def reverse_array():
    if ary == []:
        print("Array is Empty")
    else:
        for i in ary:
            print(ary[::-1])
            break
reverse_array()


# In[43]:


reverse_array()


# In[54]:


def reverse_ary():
    count = len(ary)-1
    print("Reversed Array :- ")
    for i in range(len(ary)):
        print(i,ary[count])
        count -= 1


# In[55]:


len(ary)


# In[56]:


reverse_ary()


# In[ ]:




