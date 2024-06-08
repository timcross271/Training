#Calulate dice probability for an n-sided dice. And then if the dice is rolled multiple times

#1 in 6 probability

sides=int(input('Please input number of sides on dice '))
number_dice=int(input('Please input number of dice '))
rolls=int()

probability=0
probability_mutiple=0
probability=round((1/sides)*100,2)
probability_mutiple=round((1/sides**number_dice)*100,2)

print('Probability of 1 dice',probability,'%')
print('Probability of',number_dice,'dice ',probability_mutiple,'%')