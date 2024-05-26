mylist=[10,5,2,6,7,10,15]
mylen=len(mylist)


total=0
# method 1
for number in mylist:
    total=total+number

answer=total/mylen
print(answer)


total=0
# method 2
for p in range(mylen):
    total=total+mylist[p]

answer=total/mylen
print(answer)


total=0
# method 3
count = 0
while count<mylen:
    total=total+mylist[count]
    count=count+1

print('method4:')
# method 4
for p,number in enumerate(mylist):
    total=total+number
    print(p,number)

print('answer:')
answer=total/mylen
print(answer)