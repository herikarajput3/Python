dict1 = {
    "name": "Herika",
    "age": 20
}

# Clear: it is used to remove all the elements from the dictionary
# dict1.clear()
# print(dict1)

# items: it is used to return a list of tuples containing the key-value pairs of the dictionary and it does not change the original dictionary
# print(dict1.items())

# keys: it is used to return a list of the keys of the dictionary and it does not change the original dictionary
# print(dict1.keys())

# values: it is used to return a list of the values of the dictionary and it does not change the original dictionary
# print(dict1.values())

# setDefault: it is used to set the value of a key if it is not present in the dictionary and it change the original dictionary
# dict1.setdefault("address", "Ahmedabad")
# print(dict1)

# copy: it is used to return a copy of the dictionary and returns a new dictionary
# dict2 = dict1.copy()
# print(dict2)

# update: it is used to update the dictionary with the elements of another dictionary and it change the original dictionary
# dict2 = {
#     "address": "Ahmedabad",
#     "phone": "1234567890"
# }
# dict1.update(dict2)
# print(dict1)

# formkeys: it is used to create a new dictionary with the keys from the iterable and the values as None and it does not change the original dictionary
# dict3 = dict.fromkeys(["name", "age"])
# print(dict3)

# pop: it is used to remove the key-value pair from the dictionary and it change the original dictionary
# dict1.pop("name") # it takes the key as an argument
# print(dict1)

# get: it is used to return the value of the key if it is present in the dictionary and it does not change the original dictionary
# print(dict1.get("age"))

# popitem: it is used to remove the last key-value pair from the dictionary and it change the original dictionary
# dict1.popitem()
# print(dict1)

# the difference between pop and popitem is that pop takes the key as an argument and popitem does not take any argument