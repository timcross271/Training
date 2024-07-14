import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_linear_regression.txt')

#Define range of bins

#Find max of x and f(x)
for number in input_data:






#Find all data points in each bin

#Find mean of x for each bin
#Find mean of f(x) for each bin
#Find standard deviation of f(x) for each bin (average distance from mean - error bar)
#Make new data vector - binned mean x, mean f(x), standard deviation
#Plot error bar

#Create a function for Chi Squared
#- Gets distance between data and theory(best fit) weighted with error bars, smaller bars, less error, more significance

#Chi Squared fitting, Linear Regression - Get best fit line for new binned data vector using chi squared