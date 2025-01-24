#create and calling function
def function():
    print("hallowwww")

function()

#argument
def function(name, last):
    print(name + " " + last)

function("akmal", "fayyazi")

#arbitrary argument
def fuction(*kids):
  print("The youngest child is " + kids[1])

fuction("Emil", "Tobias", "Linus")

#keyword argument
def function(child3, child2, child1):
  print("The youngest child is " + child1)

function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#arbitrary keyword argument
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#pasing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#the pass statement
def myfunction():
  pass

#position only argument
def my_function(x, /):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

#keyword only argument
def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(x):
  print(x)

my_function(3)

#combine
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
