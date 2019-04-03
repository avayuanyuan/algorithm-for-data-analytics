
# coding: utf-8

# In[10]:


import sys
import argparse
import random
import numpy as np 
import time
import math
sys.setrecursionlimit(3000)
import matplotlib.pyplot as plt


# In[11]:


# sort the array and pick the k-th smallest element from the sorted-array
def sort_and_select(current_array, k) :
    # sort the array
    sorted_current_array = np.sort(current_array,axis=None)
    return sorted_current_array[int(k)]


# In[12]:


def deterministic_select_5(current_array, k) :
    if (len(current_array) <= 5) :
        # just use any method to pick the k-th smallest element in the array
        # I am using the sort-and-select method here
        return sort_and_select(current_array, k)
    else : 
        # I need this array to compute the median-of-medians...
        medians_of_smaller_arrays_of_size_five = []
        
        # first, split current_array into smaller arrays with 5 elements each
        # there might be a better way than what I am doing... but this will work... 
        for i in range(0,len(current_array),5):
            smaller_array_of_size_five = []
            smaller_array_of_size_five.extend([current_array[i]])
            if ((i + 1) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+1]])
            if ((i + 2) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+2]])
            if ((i + 3) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+3]])
            if ((i + 4) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+4]])
            
            # we need each of these cases as len(smaller_array_of_size_five) can be anything between 1 and 5
            # based on len(smaller_array_of_size_five) we are computing the median of smaller_array_of_size_five for each case
            if (len(smaller_array_of_size_five) == 5) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,3)])
            if (len(smaller_array_of_size_five) == 4) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,2)+sort_and_select(smaller_array_of_size_five,3))//2])
            if (len(smaller_array_of_size_five) == 3) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,2)])
            if (len(smaller_array_of_size_five) == 2) :
                medians_of_smaller_arrays_of_size_five.extend([(smaller_array_of_size_five[0]+smaller_array_of_size_five[1])//2])
            if (len(smaller_array_of_size_five) == 1) :
                medians_of_smaller_arrays_of_size_five.extend([smaller_array_of_size_five[0]])

        # compute the meadian of the medians_of_smaller_arrays_of_size_five array by recursion
        p = deterministic_select_5(medians_of_smaller_arrays_of_size_five, int(len(medians_of_smaller_arrays_of_size_five)/2))
        # split the current_array into three sub-arrays: Less_than_p, Equal_to_p and Greater_than_p
        Less_than_p = []
        Equal_to_p = []
        Greater_than_p = []
        for x in current_array : 
            if (x < p) : 
                Less_than_p.extend([x])
            if (x == p) : 
                Equal_to_p.extend([x])
            if (x > p) : 
                Greater_than_p.extend([x])
                
        if (k < len(Less_than_p)) :
            return deterministic_select_5(Less_than_p, k)
        elif (k >= len(Less_than_p) + len(Equal_to_p)) : 
            return deterministic_select_5(Greater_than_p, k - len(Less_than_p) - len(Equal_to_p))
        else :
            return p


# In[13]:


def deterministic_select_7(current_array, k) :
    if (len(current_array) <= 7) :
        # just use any method to pick the k-th smallest element in the array
        # I am using the sort-and-select method here
        return sort_and_select(current_array, k)
    else : 
        # I need this array to compute the median-of-medians...
        medians_of_smaller_arrays_of_size_five = []
        
        # first, split current_array into smaller arrays with 5 elements each
        # there might be a better way than what I am doing... but this will work... 
        for i in range(0,len(current_array),7):
            smaller_array_of_size_five = []
            smaller_array_of_size_five.extend([current_array[i]])
            if ((i + 1) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+1]])
            if ((i + 2) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+2]])
            if ((i + 3) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+3]])
            if ((i + 4) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+4]])
            if ((i + 5) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+5]])
            if ((i + 6) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+6]])
            
            # we need each of these cases as len(smaller_array_of_size_five) can be anything between 1 and 5
            # based on len(smaller_array_of_size_five) we are computing the median of smaller_array_of_size_five for each case
            if (len(smaller_array_of_size_five) == 7) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,4)])
            if (len(smaller_array_of_size_five) == 6) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,3)+sort_and_select(smaller_array_of_size_five,2))//2])
            if (len(smaller_array_of_size_five) == 5) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,3)])
            if (len(smaller_array_of_size_five) == 4) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,2)+sort_and_select(smaller_array_of_size_five,3))//2])
            if (len(smaller_array_of_size_five) == 3) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,2)])
            if (len(smaller_array_of_size_five) == 2) :
                medians_of_smaller_arrays_of_size_five.extend([(smaller_array_of_size_five[0]+smaller_array_of_size_five[1])//2])
            if (len(smaller_array_of_size_five) == 1) :
                medians_of_smaller_arrays_of_size_five.extend([smaller_array_of_size_five[0]])

        # compute the meadian of the medians_of_smaller_arrays_of_size_five array by recursion
        p = deterministic_select_7(medians_of_smaller_arrays_of_size_five, int(len(medians_of_smaller_arrays_of_size_five)/2))
        # split the current_array into three sub-arrays: Less_than_p, Equal_to_p and Greater_than_p
        Less_than_p = []
        Equal_to_p = []
        Greater_than_p = []
        for x in current_array : 
            if (x < p) : 
                Less_than_p.extend([x])
            if (x == p) : 
                Equal_to_p.extend([x])
            if (x > p) : 
                Greater_than_p.extend([x])
                
        if (k < len(Less_than_p)) :
            return deterministic_select_7(Less_than_p, k)
        elif (k >= len(Less_than_p) + len(Equal_to_p)) : 
            return deterministic_select_7(Greater_than_p, k - len(Less_than_p) - len(Equal_to_p))
        else :
            return p


# In[14]:


def deterministic_select_9(current_array, k) :
    if (len(current_array) <= 9) :
        # just use any method to pick the k-th smallest element in the array
        # I am using the sort-and-select method here
        return sort_and_select(current_array, k)
    else : 
        # I need this array to compute the median-of-medians...
        medians_of_smaller_arrays_of_size_five = []
        
        # first, split current_array into smaller arrays with 5 elements each
        # there might be a better way than what I am doing... but this will work... 
        for i in range(0,len(current_array),9):
            smaller_array_of_size_five = []
            smaller_array_of_size_five.extend([current_array[i]])
            if ((i + 1) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+1]])
            if ((i + 2) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+2]])
            if ((i + 3) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+3]])
            if ((i + 4) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+4]])
            if ((i + 5) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+5]])
            if ((i + 6) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+6]])
            if ((i + 7) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+7]])
            if ((i + 8) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+8]])
            
            # we need each of these cases as len(smaller_array_of_size_five) can be anything between 1 and 5
            # based on len(smaller_array_of_size_five) we are computing the median of smaller_array_of_size_five for each case
            if (len(smaller_array_of_size_five) == 9) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,5)])
            if (len(smaller_array_of_size_five) == 8) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,4)+sort_and_select(smaller_array_of_size_five,5))//2])
            if (len(smaller_array_of_size_five) == 7) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,4)])
            if (len(smaller_array_of_size_five) == 6) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,3)+sort_and_select(smaller_array_of_size_five,2))//2])
            if (len(smaller_array_of_size_five) == 5) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,3)])
            if (len(smaller_array_of_size_five) == 4) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,2)+sort_and_select(smaller_array_of_size_five,3))//2])
            if (len(smaller_array_of_size_five) == 3) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,2)])
            if (len(smaller_array_of_size_five) == 2) :
                medians_of_smaller_arrays_of_size_five.extend([(smaller_array_of_size_five[0]+smaller_array_of_size_five[1])//2])
            if (len(smaller_array_of_size_five) == 1) :
                medians_of_smaller_arrays_of_size_five.extend([smaller_array_of_size_five[0]])

        # compute the meadian of the medians_of_smaller_arrays_of_size_five array by recursion
        p = deterministic_select_9(medians_of_smaller_arrays_of_size_five, int(len(medians_of_smaller_arrays_of_size_five)/2))
        # split the current_array into three sub-arrays: Less_than_p, Equal_to_p and Greater_than_p
        Less_than_p = []
        Equal_to_p = []
        Greater_than_p = []
        for x in current_array : 
            if (x < p) : 
                Less_than_p.extend([x])
            if (x == p) : 
                Equal_to_p.extend([x])
            if (x > p) : 
                Greater_than_p.extend([x])
                
        if (k < len(Less_than_p)) :
            return deterministic_select_9(Less_than_p, k)
        elif (k >= len(Less_than_p) + len(Equal_to_p)) : 
            return deterministic_select_9(Greater_than_p, k - len(Less_than_p) - len(Equal_to_p))
        else :
            return p


# In[18]:


def deterministic_select_11(current_array, k) :
    if (len(current_array) <= 11) :
        # just use any method to pick the k-th smallest element in the array
        # I am using the sort-and-select method here
        return sort_and_select(current_array, k)
    else : 
        # I need this array to compute the median-of-medians...
        medians_of_smaller_arrays_of_size_five = []
        
        # first, split current_array into smaller arrays with 5 elements each
        # there might be a better way than what I am doing... but this will work... 
        for i in range(0,len(current_array),11):
            smaller_array_of_size_five = []
            smaller_array_of_size_five.extend([current_array[i]])
            if ((i + 1) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+1]])
            if ((i + 2) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+2]])
            if ((i + 3) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+3]])
            if ((i + 4) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+4]])
            if ((i + 5) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+5]])
            if ((i + 6) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+6]])
            if ((i + 7) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+7]])
            if ((i + 8) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+8]])
            if ((i + 9) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+9]])
            if ((i + 10) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+10]])
        
            # we need each of these cases as len(smaller_array_of_size_five) can be anything between 1 and 5
            # based on len(smaller_array_of_size_five) we are computing the median of smaller_array_of_size_five for each case
            if (len(smaller_array_of_size_five) == 11) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,6)])
            if (len(smaller_array_of_size_five) == 10) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,5)+sort_and_select(smaller_array_of_size_five,6))//2])
            if (len(smaller_array_of_size_five) == 9) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,5)])
            if (len(smaller_array_of_size_five) == 8) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,4)+sort_and_select(smaller_array_of_size_five,5))//2])
            if (len(smaller_array_of_size_five) == 7) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,4)])
            if (len(smaller_array_of_size_five) == 6) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,3)+sort_and_select(smaller_array_of_size_five,2))//2])
            if (len(smaller_array_of_size_five) == 5) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,3)])
            if (len(smaller_array_of_size_five) == 4) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,2)+sort_and_select(smaller_array_of_size_five,3))//2])
            if (len(smaller_array_of_size_five) == 3) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,2)])
            if (len(smaller_array_of_size_five) == 2) :
                medians_of_smaller_arrays_of_size_five.extend([(smaller_array_of_size_five[0]+smaller_array_of_size_five[1])//2])
            if (len(smaller_array_of_size_five) == 1) :
                medians_of_smaller_arrays_of_size_five.extend([smaller_array_of_size_five[0]])

        # compute the meadian of the medians_of_smaller_arrays_of_size_five array by recursion
        p = deterministic_select_11(medians_of_smaller_arrays_of_size_five, int(len(medians_of_smaller_arrays_of_size_five)/2))
        # split the current_array into three sub-arrays: Less_than_p, Equal_to_p and Greater_than_p
        Less_than_p = []
        Equal_to_p = []
        Greater_than_p = []
        for x in current_array : 
            if (x < p) : 
                Less_than_p.extend([x])
            if (x == p) : 
                Equal_to_p.extend([x])
            if (x > p) : 
                Greater_than_p.extend([x])
                
        if (k < len(Less_than_p)) :
            return deterministic_select_11(Less_than_p, k)
        elif (k >= len(Less_than_p) + len(Equal_to_p)) : 
            return deterministic_select_11(Greater_than_p, k - len(Less_than_p) - len(Equal_to_p))
        else :
            return p


# In[19]:


def deterministic_select_13(current_array, k) :
    if (len(current_array) <= 13) :
        # just use any method to pick the k-th smallest element in the array
        # I am using the sort-and-select method here
        return sort_and_select(current_array, k)
    else : 
        # I need this array to compute the median-of-medians...
        medians_of_smaller_arrays_of_size_five = []
        
        # first, split current_array into smaller arrays with 5 elements each
        # there might be a better way than what I am doing... but this will work... 
        for i in range(0,len(current_array),13):
            smaller_array_of_size_five = []
            smaller_array_of_size_five.extend([current_array[i]])
            if ((i + 1) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+1]])
            if ((i + 2) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+2]])
            if ((i + 3) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+3]])
            if ((i + 4) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+4]])
            if ((i + 5) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+5]])
            if ((i + 6) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+6]])
            if ((i + 7) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+7]])
            if ((i + 8) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+8]])
            if ((i + 9) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+9]])
            if ((i + 10) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+10]])
            if ((i + 11) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+11]])
            if ((i + 12) < len(current_array)) :
                smaller_array_of_size_five.extend([current_array[i+12]])
            
            # we need each of these cases as len(smaller_array_of_size_five) can be anything between 1 and 5
            # based on len(smaller_array_of_size_five) we are computing the median of smaller_array_of_size_five for each case
            if (len(smaller_array_of_size_five) == 13) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,7)])
            if (len(smaller_array_of_size_five) == 12) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,6)+sort_and_select(smaller_array_of_size_five,7))//2])
            if (len(smaller_array_of_size_five) == 11) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,6)])
            if (len(smaller_array_of_size_five) == 10) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,5)+sort_and_select(smaller_array_of_size_five,6))//2])
            if (len(smaller_array_of_size_five) == 9) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,5)])
            if (len(smaller_array_of_size_five) == 8) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,4)+sort_and_select(smaller_array_of_size_five,5))//2])
            if (len(smaller_array_of_size_five) == 7) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,4)])
            if (len(smaller_array_of_size_five) == 6) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,3)+sort_and_select(smaller_array_of_size_five,2))//2])
            if (len(smaller_array_of_size_five) == 5) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,3)])
            if (len(smaller_array_of_size_five) == 4) :
                medians_of_smaller_arrays_of_size_five.extend([(sort_and_select(smaller_array_of_size_five,2)+sort_and_select(smaller_array_of_size_five,3))//2])
            if (len(smaller_array_of_size_five) == 3) :
                medians_of_smaller_arrays_of_size_five.extend([sort_and_select(smaller_array_of_size_five,2)])
            if (len(smaller_array_of_size_five) == 2) :
                medians_of_smaller_arrays_of_size_five.extend([(smaller_array_of_size_five[0]+smaller_array_of_size_five[1])//2])
            if (len(smaller_array_of_size_five) == 1) :
                medians_of_smaller_arrays_of_size_five.extend([smaller_array_of_size_five[0]])

        # compute the meadian of the medians_of_smaller_arrays_of_size_five array by recursion
        p = deterministic_select_13(medians_of_smaller_arrays_of_size_five, int(len(medians_of_smaller_arrays_of_size_five)/2))
        # split the current_array into three sub-arrays: Less_than_p, Equal_to_p and Greater_than_p
        Less_than_p = []
        Equal_to_p = []
        Greater_than_p = []
        for x in current_array : 
            if (x < p) : 
                Less_than_p.extend([x])
            if (x == p) : 
                Equal_to_p.extend([x])
            if (x > p) : 
                Greater_than_p.extend([x])
                
        if (k < len(Less_than_p)) :
            return deterministic_select_13(Less_than_p, k)
        elif (k >= len(Less_than_p) + len(Equal_to_p)) : 
            return deterministic_select_13(Greater_than_p, k - len(Less_than_p) - len(Equal_to_p))
        else :
            return p


# In[46]:



for num in range(1,10):
    number_of_trials=100
    array_size=1000
    k=num*array_size/2
    mean_running_time_5=[]
    mean_running_time_7=[]
    mean_running_time_9=[]
    mean_running_time_11=[]
    mean_running_time_13=[]
    for i in range(number_of_trials):
        my_array = [random.randint(1,100*array_size) for x in range(array_size*num)]
        t2=time.time()
        deterministic_select_5(my_array,k)
        t3=time.time()
        mean_running_time_5.append(t3-t2)
        t4=time.time()
        deterministic_select_7(my_array,k)
        t5=time.time()
        mean_running_time_7.append(t5-t4)
        t6=time.time()
        deterministic_select_9(my_array,k)
        t7=time.time()
        mean_running_time_9.append(t7-t6)
        t8=time.time()
        deterministic_select_11(my_array,k)
        t9=time.time()
        mean_running_time_11.append(t9-t8)
        t10=time.time()
        deterministic_select_13(my_array,k)
        t11=time.time()
        mean_running_time_13.append(t11-t10)
    
    a5=np.mean(mean_running_time_5,axis=None)
    a7=np.mean(mean_running_time_7,axis=None)
    a9=np.mean(mean_running_time_9,axis=None)
    a11=np.mean(mean_running_time_11,axis=None)
    a13=np.mean(mean_running_time_13,axis=None)

    y_axis=[a5,a7,a9,a11,a13]


    x_axis=[i for i in range(5,15,2)]

    plt.figure()
    plt.plot(x_axis,y_axis,'r')
    plt.title("Array_size="+str(array_size*num))
    plt.show()


# In[ ]:




