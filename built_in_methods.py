# abs: Returns the absolute value of a number.
print("Absolute method\n")
print(abs(-5)) 

# all: Returns True if all elements of the iterable are true (or if the iterable is empty).
print("\nAll method\n")
print(all([True, True, False]))  
print(all([True, True, True]))   
print(all([1,2,3,4,5,-44]))  # True because all numbers are non-zero
print(all([]))  # True because the iterable is empty
print(all([0, 1, 2]))  # False because 0 is false

# any: Returns True if any element of the iterable is true. If the iterable is empty, returns False.
print("\nAny method\n")
print(any([True, False, False]))  # True because at least one element is true
print(any([False, False, False]))  # False because all elements are false
print(any([0, 1, 2]))  # True because 1 and 2 are true
print(any([]))  # False because the iterable is empty
print(any((3, 2, 45, False)))  # True because 3, 2, and 45 are true
print(any((0,False)))  # False because all elements are false

# bin: Converts an integer number to a binary string prefixed with "0b".
print("\nBin method\n")
print(bin(5))
print(bin(10))
print(bin(0))

# bool: Converts a value to a Boolean, using the standard truth testing procedure.
print("\nBool method\n")
print(bool(1))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool("Hello"))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# int: Converts a value to an integer.
print("\nInt method\n")
print(int(1.5))  # 1
print(int("123"))  # 123
# print(int("abc"))  # ValueError because invalid literal for int() with base 10: 'abc'

# tuple: Converts a value into a tuple.
print("\nTuple method\n")
print(tuple([1, 2, 3]))  
print(tuple("Hello"))  
print(tuple()) 

# list: Converts a value into a list.
print("\nList method\n")
print(list((1, 2, 3)))  
print(list("Hello"))  
print(list())  

# set: Converts a value into a set.
print("\nSet method\n")
print(set([1, 2, 3, 2, 1]))  
print(set("Hello"))  
print(set())  

# dict: Converts a value into a dictionary.
print("\nDict method\n")
print(dict([("a", 1), ("b", 2), ("c", 3)]))  
print(dict.fromkeys(["a", "b", "c"], 0))  
print(dict()) 

# float: Converts a value to a floating-point number.
print("\nFloat method\n")
print(float(1))  # 1.0
print(float("123.45"))  # 123.45
# print(float("abc"))  # ValueError because could not convert string to float: 'abc'

# str: Converts a value to a string.
print("\nStr method\n")
print(str(1)) 
a = 12.2
str(a)
print(type(str(a))) 
print(str(True))  
print(type(str(True))) 

#type: It returns the type of an object.
print("\nType method\n")
print(type(1)) 
print(type(1.0))  
print(type("Hello"))  
print(type([1, 2, 3]))  
print(type((1, 2, 3)))  
print(type({1, 2, 3})) 
print(type({"a": 1, "b": 2})) 

# print: It outputs the string representation of an object.
print("\nPrint method\n")
print(1) 
print(1.0)  
print("Hello")  
print([1, 2, 3])  
print((1, 2, 3))  
print({1, 2, 3}) 
print({"a": 1, "b": 2}) 

# print method has parameters
print("Hey","Herika",sep=", ", end="!!", flush=True) # Custom flush
print('\n')

# chr: Converts an integer to its corresponding Unicode character.
print("\nChr method\n")
print(chr(97))  # 'a'
print(chr(65))  # 'A'
print(chr(8364))  # '€'

# ord: Converts a Unicode character to its corresponding integer.
print("\nOrd method\n")
print(ord('a'))  # 97
print(ord('A'))  # 65
print(ord('€'))  # 8364

# dir: Attempts to return a list of valid attributes for that object.
print("\nDir method\n")
print(dir(list()))  # List of attributes for list objects

# eval: Executes a string expression and returns the result.
print("\nEval method\n")
print(eval("1 + 1"))  # 2: Addition
print(eval("sum([1, 2, 3])"))  # 6: Sum of list
print(eval("list([1,2,3])"))  # [1, 2, 3]: List creation

# help: Invokes the built-in help system.
print("\nHelp method\n")
# help(eval)

# len: Returns the number of items in an object.
print("\nLen method\n")
print(len("Hello Herika"))  # 12
print(len([1, 2, 3]))  # 3
print(len((1, 2, 3)))  # 3
print(len({1, 2, 3}))  # 3
print(len({"a": 1, "b": 2}))  # 2