mylist=[100.25,101,98.52,96.75,102.9]
mylen=len(mylist)
total=0
total1=0

for number in mylist:
    total=total+number
average=total/mylen
print('Average',average)

for number2 in mylist:
    total1=total1+pow((number2-average),2)
    print(total1)
variance=total1/mylen
standard_deviation=pow(variance,0.5)
print('Variance',variance)
print('Standard deviation',standard_deviation)