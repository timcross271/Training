import numpy as np
import matplotlib.pylab as pl

input_data=np.loadtxt('data_for_for_loops.txt')
# print(input_data)

# input_data=input_data.flatten()
# print(input_data)

number=0

for number in input_data:
    print(int(number))
    