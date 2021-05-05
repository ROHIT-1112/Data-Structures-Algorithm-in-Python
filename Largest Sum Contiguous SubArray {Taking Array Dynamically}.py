#!/usr/bin/env python
# coding: utf-8

# In[1]:


def kadane_dynamic():
    ary = []
    val = int(input("How many elements do you want :- "))
    for i in range(val):
        do = int(input("Enter Element :- "))
        ary.append(do)
    print("The array elements are :- {}".format(ary))
    
# Kadane Algoritms :- 
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

    
kadane_dynamic()


# 
