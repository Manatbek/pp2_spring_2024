#ex1 Print the second item in the fruits list.
fruits = ["strawberry", "melon", "cherry"]
print(fruits[1])

#ex2 Change the value from "strawberry" to "kiwi", in the fruits list.
fruits = ["strawberry", "banana", "cherry"]
fruits[0] = "kiwi"

#ex3 Use the append method to add "melon" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("melon")

#ex4 Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#ex5 Use the remove method to remove "lemon" from the fruits list.
fruits = ["lemon", "banana", "cherry"]
fruits.remove("lemon")

#ex6 Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#ex7 Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#ex8 Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))