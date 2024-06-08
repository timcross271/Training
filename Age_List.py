#Find the Difference in Age between Oldest and Youngest Family Members

age_list=[]
oldest=0
youngest=500
difference=0

while 'end' not in age_list:
    age_list.append(input('Please enter age, or end to finish '))
    if 'end' in age_list:
        print('End found')
age_list.remove('end')
age_list=list(map(int,age_list))
print(age_list)


for age in age_list:
        if age>=oldest:
            oldest=age
print('The oldest is',oldest)

for age in age_list:
        if age<=youngest:
            youngest=age
print('The youngest is',youngest)

difference=oldest-youngest
print('The difference between the youngest and oldest is ',difference)