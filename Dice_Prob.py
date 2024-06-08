#Calulate dice probability for an n-sided dice. And then if the dice is rolled multiple times

#1 in 6 probability

sides=int(input('Please input number of sides on dice '))
rolls=int()

probability=0
probability=round((1/sides)*100,2)
print(probability,'%')