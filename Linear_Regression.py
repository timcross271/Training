import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_linear_regression_1000.txt')

#print(input_data[:,1])

def linear(a,b,x):
    y=a*x+b
    return y

#Use line with lowest total
#Create a new grid with a smaller range, repeat until accurate line obtained

n_grid=200
a=np.linspace(-1,-2,n_grid)
b=np.linspace(4,5,n_grid)
A,B=np.meshgrid(a,b)
A=A.flatten()
B=B.flatten()
# print(A)
# print(B)

x=input_data[:,0]
distance_list=[]
for number_A,number_B in zip(A,B):
    y=linear(number_A,number_B,x)
    distance_total=0
    for count,y_data in enumerate(input_data[:,1]):
        y_distance=y[count]-y_data
        distance_total=distance_total+abs(y_distance)
    distance_list.append(distance_total)

def line_finder (inputlist):  
    lowest=inputlist[0]
    for q,p in enumerate(range(len(inputlist)-1)):
        if abs(lowest)>abs(inputlist[p+1]):
            lowest=inputlist[p+1]
            lowest_pos=q
    return lowest_pos,lowest

best_fit,lowest_dist=line_finder(distance_list)
print(best_fit,lowest_dist)

y=linear(A[best_fit],B[best_fit],x)
print(A[best_fit])
print(B[best_fit])
      

pl.plot(x,y)
#pl.scatter(input_data[:,0],input_data[:,1],label='Data',marker='x',c='g')
pl.xlabel('X')
pl.ylabel('f(X)')
pl.legend()
pl.savefig('data_lr.jpg')
pl.show()





