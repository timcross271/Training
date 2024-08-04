import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_linear_regression_1000.txt')

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

new_data=[]
for count in range(bin_number):
    bin_x=0
    bin_y=0
    n_bin=0
    mean_bin_x=0
    mean_bin_y=0
    sigma2=0
    
    for number in input_data:
        if number[0]>bin_list[count] and number[0]<bin_list[count+1] :
            bin_x=bin_x+number[0]
            bin_y=bin_y+number[1]
            n_bin=n_bin+1
    mean_bin_x=bin_x/n_bin
    mean_bin_y=bin_y/n_bin

    #Find standard deviation of f(x) for each bin (average distance from mean - error bar)
    for number in input_data:
        if number[0]>bin_list[count] and number[0]<bin_list[count+1] :
            sigma2=sigma2+((number[1]-mean_bin_y)**2)/n_bin

    print(n_bin)
    print(mean_bin_x)
    print(mean_bin_y)
    print(sigma2)
    new_data.append([mean_bin_x,mean_bin_y,sigma2])
print(new_data)

#Make new data vector - binned mean x, mean f(x), standard deviation
new_data=np.array(new_data)
print(new_data)

#Plot error bar

pl.plot(new_data[:,0],new_data[:,1])
pl.scatter(input_data[:,0],input_data[:,1],label='Data',marker='x',c='g')
pl.errorbar(new_data[:,0],new_data[:,1],yerr=np.sqrt(new_data[:,2]))
pl.xlabel('X')
pl.ylabel('f(X)')
pl.legend()
pl.savefig('data_cs.jpg')
pl.show()

    

#Create a function for Chi Squared
#- Gets distance between data and theory(best fit) weighted with error bars, smaller bars, less error, more significance

#Chi Squared fitting, Linear Regression - Get best fit line for new binned data vector using chi squared