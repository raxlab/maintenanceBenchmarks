#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2021.07.26

@author: Anthony D. Cho
"""

## Libraires dependencies
from numpy import array
from numpy.random import seed
from scipy.stats import norm
from pandas import read_excel

## Customized function
"""                                                                ********
    Sampling from normal function
"""

def samplingFromNormal(mus, scale = 1.0, scenarios = 1, integer=True, random_seed=None):
    """
        DESCRIPTION:
            Sampling from normal distribution for each mu in mus 
            with a fixed standard deviation
            
        INPUT:
            @param mus: list of mu for gaussian distribution
            @type mus: pandas.Series, list or numpy.ndarray
            
            @param scale: standard deviation.
            @type scale: float or array
            
            @param scenarios: number of scenarios to generate (by default 1)
            @type scenarios: int
            
            @param random_seed: random seed
            @type random_seed: int
        
        OUTPUT:
            @param samples: list of samples per scenario (scenario, samples)
            @type samples: numpy.ndarray
    """
    
    if random_seed is not None:
        seed(random_seed)
    
    ## Probability function
    prob = norm
    
    ## Samples allocation
    samples = []
    
    if isinstance(scale, int) | isinstance(scale, float):
        ## Generate scenarios
        if integer:
            for _ in range(scenarios):
                samples.append( [int(max(prob.rvs(loc=mu, scale=scale), 0)) for mu in mus] )
        else:
            for _ in range(scenarios):
                samples.append( [max(prob.rvs(loc=mu, scale=scale), 0) for mu in mus] )

    else:
        ## Generate scenarios (both mus and scale as array)
        if integer:
            for _ in range(scenarios):
                samples.append( [int(max(prob.rvs(loc=mu, scale=sigma), 0)) for mu, sigma in zip(mus, scale)] )
        else:
            for _ in range(scenarios):
                samples.append( [max(prob.rvs(loc=mu, scale=sigma), 0) for mu, sigma in zip(mus, scale)] )
        
    ## return samples
    return array(samples)

"""
    Main program
"""

nComponents = 26
FILENAME = 'datasets.xls'
SHEET = f'Problem_{nComponents}'

## Load data
data = read_excel(io=FILENAME, sheet_name=SHEET)

## RUL-sampling from a normal distribution
num_scenarios = 100

RULs = samplingFromNormal(mus=data['RUL'], 
                          scale=6, ## standard deviation
                          scenarios=num_scenarios, 
                          integer=True, ## return as integer
                          random_seed=100)

