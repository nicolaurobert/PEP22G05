#String and String methods
my_var = 'Robert'

my_str = u"abcd"

my_str = f"My name is {my_var}"
print(my_str)


my_str = r"aBcD {1} \n \{1} \""
print(my_str)

result = my_str.split
print(type(result))
print(result)

result = my_str.format('x', 'y')
print(result)

result = my_str.lower()
print(result)
result = my_str.upper()
print(result)