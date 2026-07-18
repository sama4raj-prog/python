my_list1 = [1,2,3,"Python", 2.345, True, "Codingal"]
print(my_list1)

#Length of the list
print(len(my_list1))

#Accessing an item from the list
print(my_list1[3])
print(my_list1[6])

#Slicing
my_list2= my_list1[3:6]
print(my_list2)

#Iterate through a loop
for item in my_list1:
    print(item)

#Reversing a list
print(my_list1[::-1])