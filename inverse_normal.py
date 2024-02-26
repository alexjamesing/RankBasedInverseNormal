#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:36:20 2023

@author: ing
"""
import numpy as np
import scipy as scipy
import math
import scipy.special


def replace_repeated_with_mean(arr):
    """ The purpose of this script is to replace repeated values in an array, 
    with the mean of those values.
    
    """
    
    # Find the indices where the elements change
    change_indices = np.where(np.diff(arr) != 0)[0] + 1

    # Split the array into sets of repeated elements
    sets = np.split(arr, change_indices)

    # Calculate the mean of each set and replace the elements
    for i in range(len(sets)):
        set_mean = np.mean(sets[i])
        sets[i].fill(set_mean)

    # Concatenate the sets back into a single array
    result = np.concatenate(sets)
    return result


def inverse_normal(X, method='Blom', repeat_val=False):
    
    """ Applies a rank-based inverse normal transform to an numpy input. The 
    method performs faster if there are no repeated values in columns. Repeated
    column values are problematic, as they cannot be ranked against one another.
    Here, they are replaced by the mean rank value. The user should specify if 
    there are repeat values in the array provided

    Inputs:
    X: A 1-D numpy array or 2-D matrix. This function transforms this input data
    so that it is normally distributed.
    c: Constant to be used in the transformation
    method: method to choose c:
    'Blom':c=3/8
    'Tukey':c=1/3
    'Bliss':c=1/2
    'Waerden':c=0
    Outputs:
    X_trans: Transformed data
    References:
    - Van der Waerden BL. Order tests for the two-sample
    problem and their power. Proc Koninklijke Nederlandse
    Akademie van Wetenschappen. Ser A. 1952; 55:453-458
    - Blom G. Statistical estimates and transformed
    beta-variables. Wiley, New York, 1958.
    - Tukey JW. The future of data analysis.
    Ann Math Stat. 1962; 33:1-67.
    - Bliss CI. Statistics in biology. McGraw-Hill,
    New York, 1967.
    ___________________________________
    Alex Ing, 2023, partly based on MATLAB scripts by 
    Anderson M. Winkler (http://brainder.org)
    
    
    """
    
    if np.sum(np.isnan(X))>0:
        raise ValueError("input contains nans")
        
    if method == 'Blom':
        c=3/8
    elif method == 'Tukey':
        c=1/3
    elif method == 'Bliss':
        c=1/2
    elif method == 'Waerden':
        c=0
    else:
        print('method unknown, using Blom as default')
        c=3/8
    
    if repeat_val==False:
    
        ix = np.argsort(X,axis=0) ## get the rank indices
        ri = np.argsort(ix,axis=0) ## get the indices of ranked values
        
        N = X.shape[0] ## get the size of the numpy array 
        p = (ri-c)/(N-2*c+1)
        X_trans = math.sqrt(2)*scipy.special.erfinv(2*p-1)
        
    else:
        ## If we have repeated values, it is necessary to loop over columns
        ## to deal with them
        
        X_trans = np.zeros(shape = X.shape)
        
        for i in range(X.shape[1]):
            print(i)
            Y = X[:,i]
            iy = np.argsort(Y,axis=0) ## get the rank indices
            ri = np.argsort(iy,axis=0) ## get the indices of ranked values
        
            N = Y.shape[0] ## get the size of the numpy array 
            p = (ri-c)/(N-2*c+1)
            Y_trans = math.sqrt(2)*scipy.special.erfinv(2*p-1)
            
            Y_trans = replace_repeated_with_mean(Y_trans)
            
            ## Here, we check for repeated values, repeated values are
            ## replaced by the mean of repeated values
            X_trans[:,i] = Y_trans
        
    return X_trans




