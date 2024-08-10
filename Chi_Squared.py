import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_linear_regression_1000.txt')

#Define range of bins

#Find max and min of x
max=input_data[0,0]
for number in input_data[:,0]:
    if number>=max:
        max=number
# print(max)

min=input_data[0,0]
for number in input_data[:,0]:
    if number<=min:
        min=number
# print(min)

#Number and bins and bin size
#bin_number=int(input('Please enter number of bins '))
bin_number=5
bin_size=(max-min)/bin_number
# print(bin_size)

#Create a list of all the edge points, distance between them is bin_size
#Each time you add bin_size to previous number then append to list

bin_list=[]
for p in range(bin_number+1):
    bin_list.append(min+(bin_size*p))
#print(bin_list)


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

    # print(n_bin)
    # print(mean_bin_x)
    # print(mean_bin_y)
    # print(sigma2)
    new_data.append([mean_bin_x,mean_bin_y,sigma2])
#print(new_data)

#Make new data vector - binned mean x, mean f(x), standard deviation
new_data=np.array(new_data)
# print(new_data)

#Plot error bar



    

#Create a function for Chi Squared
#- Gets distance between data and theory(best fit) weighted with error bars, smaller bars, less error, more significance


def chi_squared(t,d,s2):
    c=((t-d)**2)/s2
    return c

def linear(a,b,x):
    t=a*x+b
    return t

#Make list of possible a and b values

n_grid=10
a=np.linspace(-2,-1,n_grid)
b=np.linspace(5,4,n_grid)
A,B=np.meshgrid(a,b)
A=A.flatten()
B=B.flatten()


#Make line, and then a list of theory values
#Calculate chi sqaured for theory values

position=0
t_list=[]
x=new_data[:,0]
c_list=[]

for number_A,number_B in zip(A,B):
    c_total=0
    t_list=linear(number_A,number_B,x)
    for number in range(bin_number):
        c=chi_squared(t_list[number],new_data[number,1],new_data[number,2])
        c_total=c_total+c
    c_list.append(c_total)
lowest=c_list[0]
for p,number in enumerate(c_list):
    if lowest>number:
        lowest=number 
        position=p
print('Lowest Chi Squared', lowest)
print(A[position])
print(B[position])

x=new_data[:,0]
y=linear(A[position],B[position],x)

pl.title('Chi Squared Fitting to f(x)=ax+b, a='+str(round(A[position],2))+' b='+str(round(B[position],2)))
#pl.plot(new_data[:,0],new_data[:,1])
pl.scatter(input_data[:,0],input_data[:,1],marker='x',c='g',alpha=0.5,label='Data')
pl.plot(x,y,c='k',label='Theory')
pl.errorbar(new_data[:,0],new_data[:,1],yerr=np.sqrt(new_data[:,2]),c='r',ls='none',markersize=4,marker='o',capsize=5,alpha=0.7,label='Binned data')
# pl.plot(new_data[:,0],t_list,c='r')
pl.xlabel('X')
pl.ylabel('f(X)')
pl.legend()
# pl.savefig('data_cs.jpg')
pl.show()