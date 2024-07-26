import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_linear_regression.txt')

#Define range of bins

#Find max and min of x
max=input_data[0,0]
for number in input_data[:,0]:
    if number>=max:
        max=number
print(max)

min=input_data[0,0]
for number in input_data[:,0]:
    if number<=min:
        min=number
print(min)

#Number and bins and bin size
bin_number=int(input('Please enter number of bins '))
bin_size=(max-min)/bin_number
print(bin_size)

#Create a list of all the edge points, distance between them is bin_size
#Each time you add bin_size to previous number then append to list

bin_list=[]
for p in range(bin_number+1):
    bin_list.append(min+(bin_size*p))
print(bin_list)


#Find all data points in each bin
#Between bin_list[1] and bin_list[2], how many data points in input_data are there

#Find mean of x for each bin
#Find mean of f(x) for each bin
    

#Find standard deviation of f(x) for each bin (average distance from mean - error bar)
#Make new data vector - binned mean x, mean f(x), standard deviation
#Plot error bar

#Create a function for Chi Squared
#- Gets distance between data and theory(best fit) weighted with error bars, smaller bars, less error, more significance

#Chi Squared fitting, Linear Regression - Get best fit line for new binned data vector using chi squared