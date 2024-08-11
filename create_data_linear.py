import numpy as np
import matplotlib.pylab as pl

def linearfunc(x,a,b):
	return a*x+b

a = -1.2
b = 4.5

npoints = 10000
x = np.random.uniform(0,5,npoints)
theory = linearfunc(x,a,b)
noise = np.random.normal(0,1,npoints)
data = theory + noise

# pl.plot(x,theory)
pl.scatter(x, data)
pl.show()

filename = 'data_for_linear_regression_10000.txt'
np.savetxt(filename,np.array((x,data)).T,header='data for linear regression')
input_data = np.loadtxt(filename)

