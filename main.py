"""Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. 
The letters in LEGB stand for Local, Enclosing, Global, and Built-in."""

a = 1
b = 2
def some_function():
  b = 5
  print('b from function: ' + str(b))
  return b

print(a)
some_function()
print('b outside function: ' + str(b))

