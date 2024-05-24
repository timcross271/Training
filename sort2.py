#Code for sorting a list from smallest to largest number

mylist=[10,5.5,3,100,32,55,125,76,3,-5,-45]
sorted_list=[]
mylen=len(mylist)

print('list length is',mylen)


#Finds the lowest number in a list, and returns it

def lowest_finder (inputlist):  
    lowest=inputlist[0]
    for p in range(len(inputlist)-1):
        if lowest>inputlist[p+1]:
            lowest=inputlist[p+1] 
    return lowest


#Brute force sort method. 
#Goes through the list a number of times equal to the list length.
#Each time finds the smallest number, adds that number to a sorted list and removes it from the original list.

for q in range (mylen):         
    new_low=lowest_finder(mylist)
    sorted_list.append(new_low)
    mylist.remove(new_low)
print(sorted_list)   


