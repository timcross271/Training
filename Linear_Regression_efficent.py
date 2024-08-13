import numpy as np
import matplotlib.pylab as pl

##################################################################################################################
# Define functions
##################################################################################################################

def linear(a,b,x):
    y=a*x+b
    return y

def line_finder (inputlist):  
    # Old code:
    # lowest=inputlist[0]
    # for q,p in enumerate(range(len(inputlist)-1)):
    #     if abs(lowest)>abs(inputlist[p+1]):
    #         lowest=inputlist[p+1]
    #         lowest_pos=q
    # New code:
    lowest=min(inputlist)
    lowest_pos=np.argmin(inputlist)
    return lowest_pos,lowest

##################################################################################################################
# Read in data
##################################################################################################################

input_data=np.loadtxt('data_for_linear_regression_1000.txt')


##################################################################################################################
# Create grid of possible a and b values
##################################################################################################################

n_grid=200
a=np.linspace(-2,-1,n_grid)
b=np.linspace(4,5,n_grid)
A,B=np.meshgrid(a,b)
A_grid=A.flatten()
B_grid=B.flatten()

##################################################################################################################
# Find the distances from data points to theory lines (a,b)
##################################################################################################################

x=input_data[:,0]
distance_list=[]
for number_A,number_B in zip(A_grid,B_grid):
    y=linear(number_A,number_B,x)
    distance_total=0

    #Old code:
    # for count,y_data in enumerate(input_data[:,1]):
    #     y_distance=y[count]-y_data
    #     distance_total=distance_total+abs(y_distance)
    #New code:
    distance_total=(abs(y-input_data[:,1])).sum()
    distance_list.append(distance_total)

##################################################################################################################
# Find best fitting line to data
##################################################################################################################

best_fit,lowest_dist=line_finder(distance_list)
print(best_fit,lowest_dist)

y=linear(A_grid[best_fit],B_grid[best_fit],x)
print(A_grid[best_fit])
print(B_grid[best_fit])



##################################################################################################################
# Plot data points and theory line
##################################################################################################################

pl.plot(x,y)
pl.scatter(input_data[:,0],input_data[:,1],label='Data',marker='x',c='g')
pl.xlabel('X')
pl.ylabel('f(X)')
pl.legend()
pl.savefig('data_lr.jpg')
pl.show()





