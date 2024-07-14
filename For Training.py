num_list=[100,20,5,37,10,5,200,12,23]
# print(num_list)

mylen=len(num_list)
# print('Length',mylen)


# Method 1 - number is the count and the actual data/number within the list
# answer=0
# total=0
# for number in num_list:
#   answer=number*2
#   total=total+answer
#   print (answer) 
#   print(total)


#Method 2 - number is just a counter, counting the length of the list. 
# The count position is the used to reference the list position - num_list[number]


# answer=0
# total=0
# for number in range(mylen):
#     answer=num_list[number]*2
#     total=total+answer
#     print(answer)
#     print('Tot',total)


#Method 3 - Number is a count,and is again used to reference the list position. The count is advanced manually - number+1

# answer=0
# total=0
# number=0

# while number<mylen:
#     answer=num_list[number]*2
#     total=total+answer
#     print(answer)
#     print('Tot',total)
#     number=number+1


#Method 4 - p is count position, number is the actual number in the list. Can be used seperatley. 

answer=0
total=0
number=0

for p, number in enumerate(num_list):
    answer=num_list[p]*2
    print(answer)
    answer=number*2
    print(answer)
    total=total+answer
    print('Tot',total)
