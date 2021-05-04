#!/usr/bin/env python
# coding: utf-8

# # Program to Search in an Unsorted Array

# In[2]:


arr = [44,22,4,33,445]
element = int(input("Enter element to be searched :- "))
def fixed_search():
    #checking if array exists or not
    
    if arr != []:
        print("\nArray exists :- ",arr)
    elif arr == []:
        print("\narray doesn't exists")
    
    #Sorting the array
    if arr == []:
        pass
    else:
        arr.sort()
        print("\nArray sorted :- ",arr)
    
    #Finding element to be searched using brute force method
    liz = len(arr)
        
    for i in range(liz):
        if arr[i] == element:
            print("\nElement found at index :-  ",i)
            break
    if arr[i] != element:
        print("\n{} not found in Array".format(element))
    
fixed_search()


# # Program to Input element and search elements in array dynamically

# In[41]:


# Dynamic Array elements allocation and searching

def dynamic_search():
    arry = []
    i = 0
    ele = int(input("\nEnter how many elements , you want in the array :-  "))
    if ele > 0:
        while i < ele:
            val = int(input("\nEnter elements for array :- "))
            arry.append(val)
            i += 1
        print("\nEntered array elements are:- ",arry)
        
        
    if arry != []:
        print("\nArray exists")
    elif arry == []:
        print("\narray doesn't exists")
    
    
    sear = int(input("\nEnter element to be searched from the array :- "))
    
    #Sorting the array
    if arry == []:
        pass
    else:
        arry.sort()
        print("\nArray sorted :- ",arry)
    
    #Finding element to be searched using brute force method
    liz = len(arry)
        
    for i in range(liz):
        if arry[i] == sear:
            print("\nElement found at index :-  ",i)
            break
    if arry[i] != sear:
        print("\n{} not found in Array".format(sear))
        
    
dynamic_search()


# # Insert Opeartion in the array (Static)

# In[16]:


#Inserting function in an array
def insertion(): #Here element is just taking reference of the key variable
    air = [11,12,13,14]
    print("Given Array is :- ",air)
    key = int(input('Enter value to be entered in the array :- ')) #Element to be inserted
    print("Before Insertion :- ",air)
    air.append(key)
    print("After Insertion :- ",air)

insertion()


# In[33]:


if key in air :
    print("True")
else:
    print("Hello")


# # Delete Operation in Array

# In[38]:


def ary_del():
    ary = [12,19,88,77,100,27,94,101,8777,647,262]
    ary.sort()
    print("Before deleting array in sorted order :- ",ary)
    del_ele = int(input("\nEnter element to be deleted from array :- "))
    
    if del_ele in ary:
        ary.remove(del_ele)
    print("\n{} removed from array ".format(del_ele))
    print("\n\nAfter removing the value :- ",ary)
ary_del()


# ### 
