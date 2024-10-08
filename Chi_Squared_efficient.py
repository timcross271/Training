import numpy as np
import matplotlib.pylab as pl
import time

##################################################################################################################
# Read in data
##################################################################################################################

# Read in the data
input_data=np.loadtxt('data_for_linear_regression_1000.txt')

##################################################################################################################
# Setup the input parameters
##################################################################################################################

start_time = time.time()
# Priors on free parameters
a_min=-2
a_max=-1
b_min=4
b_max=5
# number of grid points
n_grid=10

#Number and bins and bin size
#bin_number=int(input('Please enter number of bins '))
bin_number=30


##################################################################################################################
# Define functions
##################################################################################################################

#Create a function for Chi Squared
#- Gets distance between data and theory(best fit) weighted with error bars, smaller bars, less error, more significance
def chi_squared(t,d,s2):
    c=((t-d)**2)/s2
    return c

# Theoretical function
def linear(a,b,x):
    t=a*x+b
    return t


##################################################################################################################
# Define bin sizes
##################################################################################################################

#Define range of bins
#Find max and min of x

# Old code:
# max=input_data[0,0]
# for number in input_data[:,0]:
#     if number>=max:
#         max=number
# print('old',max)

# New code:
max=input_data[:,0].max()
# print(max)

# Old code:
# min=input_data[0,0]
# for number in input_data[:,0]:
#     if number<=min:
#         min=number
# print(min)

# New code:
min=input_data[:,0].min()

#Create a list of all the edge points where the distance between them is bin_size
#Each time you add bin_size to previous number then append to list
# Old code:
# bin_size=(max-min)/bin_number
# bin_edges=[]
# for p in range(bin_number+1):
#     bin_edges.append(min+(bin_size*p))
# print('old',bin_edges)

# New code:
bin_edges=np.linspace(min,max,bin_number+1)
# print('new',bin_edges)


##################################################################################################################
# Find mean data points and their standard deviation for each bin
##################################################################################################################

#Find all data points in each bin
#Between bin_edges[1] and bin_edges[2], how many data points in input_data are there
#Find mean of x for each bin
#Find mean of f(x) for each bin

new_data=[]
for count in range(bin_number):
    bin_x=0
    bin_y=0
    npoints_bin=0
    meanpoints_bin_x=0
    meanpoints_bin_y=0
    sigma2=0
    
    # Old code:
    # for number in input_data:
    #     if number[0]>bin_edges[count] and number[0]<bin_edges[count+1] :
    #         bin_x=bin_x+number[0]
    #         bin_y=bin_y+number[1]
    #         npoints_bin=npoints_bin+1
    # meanpoints_bin_x=bin_x/npoints_bin
    # meanpoints_bin_y=bin_y/npoints_bin

    # #Find standard deviation of f(x) for each bin (average distance from mean - error bar)
    # for number in input_data:
    #     if number[0]>bin_edges[count] and number[0]<bin_edges[count+1] :
    #         sigma2=sigma2+((number[1]-meanpoints_bin_y)**2)/npoints_bin
    

    # New code:
    points_in_bin=((input_data[:,0]>bin_edges[count]) & (input_data[:,0]<bin_edges[count+1]))
    meanpoints_bin_x=input_data[points_in_bin,0].mean()
    meanpoints_bin_y=input_data[points_in_bin,1].mean()
    sigma2=input_data[points_in_bin,1].var()
    
    #Make new data vector - binned mean x, mean f(x), standard deviation
    new_data.append([meanpoints_bin_x,meanpoints_bin_y,sigma2])

##################################################################################################################
# Create new data vector as an array and save to file
##################################################################################################################

new_data=np.array(new_data)
np.savetxt('binned_data_for_linear_regression.txt',new_data)


##################################################################################################################
# Create grid of possible a and b values
##################################################################################################################

#Make list of possible a and b values on a grid
a=np.linspace(a_min,a_max,n_grid)
b=np.linspace(b_min,b_max,n_grid)
A,B=np.meshgrid(a,b)
A_grid=A.flatten()
B_grid=B.flatten()


##################################################################################################################
# Calculate Chi Squared for theory values (a,b)
##################################################################################################################

#Make line, and then a list of theory values
#Calculate chi sqaured for theory values
# position=0
theory_list=[]
chi2_list=[]
x=new_data[:,0]

# Loop over the a and b grid points. For each set of values make a theory line for the binned x values
# Calculate the chi2 for those theory values

# Old code:
# for number_A,number_B in zip(A_grid,B_grid):
#     chi2_total=0
#     theory_list=linear(number_A,number_B,x)
#     for counter in range(bin_number):
#         c=chi_squared(theory_list[counter],new_data[counter,1],new_data[counter,2])
#         chi2_total=chi2_total+c
#     chi2_list.append(chi2_total)


# New code:
for number_A,number_B in zip(A_grid,B_grid):
    theory_list=linear(number_A,number_B,x)
    chi2_total=(chi_squared(theory_list,new_data[:,1],new_data[:,2])).sum()
    chi2_list.append(chi2_total)
chi2_array=np.asarray(chi2_list)


##################################################################################################################
# Find best fit theory/line from Chi Squared values (lowest Chi Squared)
##################################################################################################################

# find the minimum chi2
# Old code:
# lowest=chi2_array[0]
# for p,number in enumerate(chi2_array):
#     if lowest>number:
#         lowest=number 
#         position=p
# print('Lowest Chi Squared', lowest)


# New code:
lowest=chi2_array.min()
position=np.argmin(chi2_array)

# print('Lowest Chi Squared', lowest)

print('Lowest Chi Squared %s' % lowest)
print(A_grid[position])
print(B_grid[position])

##################################################################################################################
# Plot data and theory
##################################################################################################################


y=linear(A_grid[position],B_grid[position],x)
y_lr=linear(-1.2010050251256281,4.49748743718593,x)
y_lr=linear(-1.221105527638191,4.50251256281407,x)

pl.title('Chi Squared Fitting to f(x)=ax+b, a='+str(round(A_grid[position],2))+' b='+str(round(B_grid[position],2)))
pl.scatter(input_data[:,0],input_data[:,1],marker='x',c='g',alpha=0.5,label='Data')
pl.plot(x,y,c='k',label='Theory')
pl.errorbar(new_data[:,0],new_data[:,1],yerr=np.sqrt(new_data[:,2]),c='r',ls='none',markersize=4,marker='o',capsize=5,alpha=0.7,label='Binned data')
pl.plot(x,y_lr,c='y',ls='--')
# pl.plot(new_data[:,0],theory_list,c='y')
# pl.plot(new_data[:,0],new_data[:,1],c='y')
pl.plot()
pl.xlabel('X')
pl.ylabel('f(X)')
pl.legend()
# pl.savefig('data_cs.jpg')

print("--- %s seconds ---" % (time.time() - start_time))

pl.show()