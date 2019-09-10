#!/usr/bin/env python3
# coding: utf-8

# Gibbs-Sampling procedure to compute the Probability Matrix of a Discrete-Time Markov
# Chain whose states are the d-dimensional cartesian product of the form 
# {0,1,...n-1} x {0,1,...n-1} x ... X {0,1,...n-1} (i.e. d-many products)
# 
# The target stationary distribution is expressed over the n**d many states 
#
# Written by Prof. R.S. Sreenivas for
# IE531: Algorithms for Data Analytics
#

import sys
import argparse
import random
import numpy as np 
import time
import math
import matplotlib.pyplot as plt
import itertools as it

# need this to keep the matrix print statements to 4 decimal places
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

# This function computes a random n-dimensional probability vector (whose entries sum to 1)
def generate_a_random_probability_vector(n) :
    y = np.random.uniform(0,100,n)
    y = y/np.sum(y)
    return y

# Two d-tuples x and y are Gibbs-Neighbors if they are identical, or they differ in value at just
# one coordinate
def check_if_these_states_are_gibbs_neighbors(x, y) :
    # x and y are dim-tuples -- we will assume they are not equal
    # count the number of coordinates where they differ
    #a = np.sum(np.array(x)-np.array(y) !=0 )
    a = np.where(np.array(x)!=np.array(y))[0].shape[0]
    result = True
    if a >1:
        result = False
    return result

# Given two Gibbs-Neighbors -- that are not identical -- find the coordinate where they differ in value
# this is the "free-coordinate" for this pair
def free_coordinates_of_gibbs_neighbors(x, y) :
    # we assume x and y are gibbs neighbors, then the must agree on at least (dim-1)-many coordinates
    # or, they will disagree on just one of the (dim)-many coordinates... we have to figure out which 
    # coordinate/axes is free
    free_index = np.where(np.array(x)!=np.array(y))[0][0]
    return free_index

# x in a dim-tuple (i.e. if dim = 2, it is a 2-tuple; if dim = 4, it is a 4-tuple) state of the Gibbs MC
# each of the dim-many variables in the dim-tuple take on values over range(n)... this function returns 
# the lexicographic_index (i.e. dictionary-index) of the state x
def get_lexicographic_index(x, n, dim) :
   x_ = np.array(x)
   number= x_.dot(np.power(n,np.arange(dim)[::-1]))
   return int(number)

def get_one_dim_lower_matrix(dim):
    I = np.identity(dim-1,dtype=np.int16)
    #f = {d: np.matrix(np.hstack([I[:,:d],np.zeros((dim-1,1)),I[:,d:]]) ) for d in range(dim)}
    dim_array = np.matrix(np.power(n,np.arange(dim-1)[::-1],dtype = np.int16))
    f = {d: dim_array* np.matrix(np.hstack([I[:,:d],np.zeros((dim-1,1)),I[:,d:]]) ) for d in range(dim)}
    return f

def get_one_dim_lower(x,d,matrix):
    m = matrix[d]
    return m.dot(np.array(x))

def get_one_dim_lower_index(x,d,matrix):
    return int(matrix[d].dot(np.array(x)))

def get_normalization(pi,n,dim,matrix):
    normalization = np.zeros((dim,n**(dim-1)))
    for  x in it.product(range(n),repeat = dim):
        for d in range(dim):
            #x_ = get_one_dim_lower(x,d,matrix)
            #idx = get_lexicographic_index(x_,n,dim-1)
            idx = get_one_dim_lower_index(x,d,matrix)
            normalization[d,idx] += pi[get_lexicographic_index(x,n, dim)]
    return normalization
# This is an implementaton of the Gibbs-Sampling procedure
# The MC has n**dim many states; the target stationary distribution is pi
# The third_variable_is when set to True, prints the various items involved in the procedure
# (not advisable to print for large MCs)
def create_gibbs_MC(n, dim, pi, do_want_to_print) :
    if (do_want_to_print) :
        print ("Generating the Probability Matrix using Gibbs-Sampling")
        print ("Target Stationary Distribution:")
        for x in it.product(range(n), repeat = dim) :
            number = get_lexicographic_index(x, n, dim)
            print ("\u03C0", x, " = \u03C0(", number , ") = ", pi[number])
    
    # the probability matrix will be (n**dim) x (n**dim) 
    probability_matrix = [[0 for x in range(n**dim)] for y in range(n**dim)]
    t0 = time.time()
    matrix = get_one_dim_lower_matrix(dim)
    normalization = get_normalization(pi,n,dim,matrix)
    dt = time.time() -t0
    # the state of the MC is a dim-tuple (i.e. if dim = 2, it is a 2-tuple; if dim = 4, it is a 4    -tuple)
    # got this from https://stackoverflow.com/questions/7186518/function-with-varying-number-of-for-loops-python
    count = 0
    t0 = time.time()
    for x in it.product(range(n), repeat = dim) :
        # x is a dim-tuple where each variable ranges over 0,1,...,n-1
        index_x = get_lexicographic_index(x,n,dim)
        for y in it.product(range(n), repeat = dim) :
            index_y = get_lexicographic_index(y,n,dim)
            if not (check_if_these_states_are_gibbs_neighbors(x, y)) or x==y :
                continue
            coord = free_coordinates_of_gibbs_neighbors(x, y)
            #y_ = get_one_dim_lower(y,coord,matrix)
            #remain_index = get_lexicographic_index(y_,n,dim-1)
            remain_index = get_one_dim_lower_index(y,coord,matrix)
            probability_matrix[index_x][index_y] = 1./dim * pi[index_y]/normalization[coord,remain_index]
            count +=1
            if count%10000 ==0 :
                nowtime = time.time()
                print (count,nowtime-t0)
                t0 = time.time()
    probability_matrix = np.array(probability_matrix)
    #for i in range(n**dim):
    #    probability_matrix[i,i] = 1.0 - np.sum(probability_matrix[i,:])
    np.fill_diagonal(probability_matrix, 1.0 - np.sum(probability_matrix,axis=1))
    return probability_matrix

# Trial 1... States: {(0,0), (0,1), (1,0), (1,1)} (i.e. 4 states)
n = 2
dim = 2
a = generate_a_random_probability_vector(n**dim)
print("(Random) Target Stationary Distribution\n", a)
p = create_gibbs_MC(n, dim, a, True) 
print ("Probability Matrix:")
print (np.matrix(p))
print ("Does the Probability Matrix have the desired Stationary Distribution?", np.allclose(np.matrix(a), np.matrix(a)* np.matrix(p)))

# Trial 2... States{(0,0), (0,1),.. (0,9), (1,0), (1,1), ... (9.9)} (i.e. 100 states)
n = 10
dim = 2
a = generate_a_random_probability_vector(n**dim)
p = create_gibbs_MC(n, dim, a, False) 
print ("Does the Probability Matrix have the desired Stationary Distribution?", np.allclose(np.matrix(a), np.matrix(a)* np.matrix(p)))

# Trial 3... 1000 states 
n = 10
dim = 3
t1 = time.time()
a = generate_a_random_probability_vector(n**dim)
p = create_gibbs_MC(n, dim, a, False) 
t2 = time.time()
hours, rem = divmod(t2-t1, 3600)
minutes, seconds = divmod(rem, 60)
print ("It took ", hours, "hours, ", minutes, "minutes, ", seconds, "seconds to finish this task")
print ("Does the Probability Matrix have the desired Stationary Distribution?", np.allclose(np.matrix(a), np.matrix(a)* np.matrix(p)))

# Trial 4... 10000 states 
n = 10
dim = 4
t1 = time.time()
a = generate_a_random_probability_vector(n**dim)
p = create_gibbs_MC(n, dim, a, False) 
t2 = time.time()
hours, rem = divmod(t2-t1, 3600)
minutes, seconds = divmod(rem, 60)
print ("It took ", hours, "hours, ", minutes, "minutes, ", seconds, "seconds to finish this task")
print ("Does the Probability Matrix have the desired Stationary Distribution?", np.allclose(np.matrix(a), np.matrix(a)* np.matrix(p)))

