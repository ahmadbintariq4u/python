# Variables 
x = 5
print(x)
x = 5.1
print(x)
x = 'String'
print(x)
x = False
print(x)


# Collections

mylist = ["apple", "banana", "cherry"]  # list
print(mylist)

mytuple = ("apple", "banana", "cherry") # tuple
print(mytuple)

myset = {"apple", "banana", "cherry"}   # set
print(myset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)


 
# loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(2, 6):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")


# Array
cars = ["Ford", "Volvo", "BMW"]

# Function
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")