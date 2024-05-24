import time

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
val2=int(input("Enter power of:"))
counter2=0
output=1

# while counter2<val2:
#     output=mult(val1,output)
#     print(counter2,output)
#     counter2=counter2+1
t0=time.time()
for counter2 in range(0,val2):
    output=mult(val1,output)
    #print(counter2,output)
t1=time.time()
print("Tims",output)
print(t1-t0)

#Homework - and check for numnbers being integers
#Write power code - 
#Add comments to code

counter2=0
output=1

# while counter2<val2:
#     output=mult(val1,output)
#     print(counter2,output)
#     counter2=counter2+1
t0=time.time()
for counter2 in range(0,val2):
    output=val1*output
    #print(counter2,output)
t1=time.time()

print("Comp",output)
print(t1-t0)

t0=time.time()
output=val1**val2
t1=time.time()

print("Pow",output)
print(t1-t0)
