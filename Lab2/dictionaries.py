#ex1 Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}
print(
car.get("model")
)

#ex2 Change the "year" value from 2018 to 2020.
car =	{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}
car["year"] = 2020

#ex3 Add the key/value pair "color" : "black" to the car dictionary.
car =	{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}
car["color"] ="black"

#ex4 Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}
car.pop("model")

#ex5 Use the clear method to empty the car dictionary.
car =	{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018
}
car.clear()





