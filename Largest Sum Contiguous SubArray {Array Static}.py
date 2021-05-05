#!/usr/bin/env python
# coding: utf-8

# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum. 

# In[13]:


def kadane(ary):
    maxsum = 0
    current_sum = 0
    i = 0
    liz = len(ary)
    for i in range(liz):
        current_sum = current_sum + ary[i]
        if current_sum > maxsum:
            maxsum = current_sum
        elif current_sum < maxsum:
            current_sum = 0
    print("The max sum in One dimensional subarray is :- {}".format(maxsum))

ary = [-4,3,2,-1,4,-9,11,-9]


# In[14]:


kadane(ary)


# 

# In[ ]:





# In[ ]:




