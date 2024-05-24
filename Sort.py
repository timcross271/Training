mylist=[10,5.5,3,100,32,55,125,76]
list1=[]
lowest=mylist[0]
temp2=[]
mylen=len(mylist)


print('list length is',mylen)

for q in range (mylen):
    lowest=mylist[0]
    print(q)
    for p in range(mylen-1-q):
        print(p)
        if lowest>mylist[p+1]:
            lowest=mylist[p+1] 
            print("in if")
            # print('lowest',lowest)
    print('lowest =',lowest)
    list1.append(lowest)
    print('list1',list1)
    mylist.remove(lowest)
    

# print(lowest)
# print(list1)
      
   #add temp to list
   #temp into temp2
   #check for temp2 in if loop

