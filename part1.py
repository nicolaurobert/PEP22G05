a = 100
b = 100

if a > b:
    print('a is larger')
elif a > 50:
    print('a is grater then 50')
elif a > 60:
    print('a is grater then 60')
else:
    print('b is larger')

a = "101"

if a > '100':
    print('succes >')
elif a == '100':
    print('success ==')

# chr() and ord()

print(ord('1'))
print(ord('0'))
print(ord('a'))
print(ord('A'))
print(chr(65))

# Trueish

a = "101"
print(a > '100')

if True:
    print('this will always be true')

if a:
    print('This will also always be true')

a = ""
if a:
    print('this will also always be false')
else:
    print('a is false ')

a = (0)
if a:
    print('a is True')
else:
    print('a is False')

# For loops

a = 'my_string'
a.__iter__()
for i in a:
    print(i)

# a = 100
# a.__iter__()
#
# for i in a:
#    print(i)

result = range(10)
print(result)
print(type(result))
print(result.__iter__())

for i in result:
    print(i)

# while loop
# a=100
# while a < 200:
#     print('TO iNFINITY')
#     a += 1
#     if a % 101:
#         break
#         print('after break')

a = 2
print(2 <= a <= 5)

response = int(input('select 1 to 5 '))
while not (1 <= response <= 5):
    response = int(input('select 1 to 5'))
