import sys
from pynest import Sampler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
mean = 0
dev = 2
def simulate_data(a,b,n):
    x = np.linspace(0,10,n)
    y = a*x + b + np.random.normal(loc=mean,scale=dev,size=n)
    return x,y

#x, y = simulate_data(5,10,50)
data = pd.read_csv('simulated_data.csv')
x = data['x'].values
y = data['y'].values
def log_gaussian(x, mu, sig):
    return np.log(1/np.sqrt(2 * np.pi * sig**2.0))  +  (-0.5/sig**2.0) * (x - mu)**2.0

def myloglike(cube):
    log_likelihood = 0
    for i in tuple(zip(x,y)):
        log_likelihood += log_gaussian(i[1], cube[0]*i[0] + cube[1], dev)
    return log_likelihood

def myprior(cube):
    cube[0] = cube[0] * 10
    cube[1] = cube[1] * 20
    return cube
def test_mcmc_instantation():
    sampler = Sampler(log_likelihood=myloglike, prior=myprior, ndim = 2, sample_method = 'mcmc', initial_points=20)
    sampler.sample()

print('running the example')
test_mcmc_instantation()

