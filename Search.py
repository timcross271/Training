
#Find the names position


mylist=["Tim","Marika","John","Sarah","Diane","Tim","Barry"]
search=input("Enter name:")
search_count=0


for name in mylist:
	if name==search:
		search_count=search_count+1

if search_count>=1:
	print("The name was found",search_count,"times")
else:
	print("The name was not found")

    


