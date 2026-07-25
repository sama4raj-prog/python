my_dict = {
    "name": "Rajonna",
    "grade": 7,
    "age": 13,
    "country": "Bangladesh",
}

#Length of dictionary
print(len(my_dict))

#Accessing values
print(my_dict["name"]) #method 1
print(my_dict.get("grade")) #method 2

#Adding an item
my_dict["city"] = "Chattogram"
print(my_dict)

#Update an item
my_dict["grade"] = 8
print(my_dict)

#Removing an item
my_dict.pop("country")
print(my_dict)

#Delete the dictionary
my_dict.clear()
print(my_dict)