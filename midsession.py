# Create a tuple called full_name that contains your first name and last name. 
# Convert the full_name tuple to a list.
# Reverse the full_name list so that it is last name, first name.


full_name = ("Vanessa", "Roman")
full_name1 = list(full_name)
full_name1.sort()
print full_name1

# sorted_list = sorted(full_name1)
# print sorted_list


for num in range(100,1001, 100):
	print num

list_names = ['Steven','Michael','James']
for name in list_names:
	print name + len(list_names)