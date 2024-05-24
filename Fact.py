#Factorial - Done
#Make a function, then integrate with other codes - done







def mult (a,b):
    mult_result=0
    counter=0
    if b>a:
        c=b
        b=a
        a=c
    while counter<b:
        mult_result=mult_result+a
        counter=counter+1
    return mult_result

val1=int(input("Enter number:"))
a=val1
b=val1
c=val1

for p in range(0,c-1):
    a=a-1
    b=mult(b,a)

if b==0:
    b=b+1

print(b)