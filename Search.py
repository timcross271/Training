mylist=["Tim","Marika","John","Sarah","Diane","Tim","Barry"]
pos_list=[]
search=input("Enter name:")
search_count=0

# counter=0
# for name in mylist:
# 	counter=counter+1
# 	if name==search:
# 		search_count=search_count+1
# 		pos_list.append(counter)

for counter,name in enumerate(mylist):
	if name==search:
		search_count=search_count+1
		pos_list.append(counter+1)

if search_count>=1:
	print("The name was found",search_count,"times")
	print('In positions',pos_list)
else:
	print("The name was not found")

    




