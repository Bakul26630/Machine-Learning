# Create, initialize and display simple variables and simple strings and use simple formatting for variable.
from string import Template

a = 'The great aim of education is not knowledge but action.'
name = "Bakul Garg"

# String Formatting using f-string
print(f"My name is {name}")

# String Formatting using % operator
print("My name is %s"%(name))

# String Formatting using format method
print("My name is {0}".format(name))

# String formatting using string template class
template = Template("My name is $name")
print(template.substitute(name=name))




