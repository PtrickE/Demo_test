
myString = "This is a String"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("what is you name? ")
print(name)

color = input("What is you favorite color? ")
animal = input("What is you favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))