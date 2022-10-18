import random
import string

s="adfwer332a@"
print(dir(random))
print(random.choice(s))
print(dir(string))
print(random.sample(string.ascii_uppercase, 2))
print(random.choice(string.digits))
print(random.choice(string.punctuation))
print(random.sample(string.ascii_lowercase, 6))


Dunder Functions
in python
__init__
List comprehensions
Generators..
yield
Abstract classes in python
•	HOw does dict work internally in python?
Difference between list and the tuple?
vik to Everyone (9:42 AM)
GIL
Global Intepreter Lock
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
vik to Everyone (9:45 AM)
[47,69,76,97]
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
a) 0 1
b) 0 0
c) Error
vik to Everyone (9:53 AM)
Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
Hint: dir(random)
vik to Everyone (9:59 AM)
ascii_uppercase