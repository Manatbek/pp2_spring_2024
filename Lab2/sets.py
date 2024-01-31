#ex1 Check if "banana" is present in the fruits set.
fruits = {"banana", "banana", "cherry"}
if "banana" in fruits:
  print("Yes, banana is a fruit!")

#ex2 Use the add method to add "kiwi" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("kiwi")

#ex3 Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex4 Use the remove method to remove "cherry" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("cherry")

#ex5 Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
