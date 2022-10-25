# ex1

# numar = range(int(input('Introduceti un numar: ')))
# for i in numar:
#     result = i % 2
#     if result == 0:
#         print(i)
#
# numar = range(int(input('Introduceti un numar: ')))
# for i in numar:
#     result = i % 2
#     if result != 1:
#         print(i)

# ex2

cappucino = 4
espresso = 3.5

print(f"1. cappucino...{cappucino} lei")
print(f"2 Espresso...{espresso} lei  ")
optiune = input("ce optiuni alegeti? [1,2]").strip()
bancnota = int(input("introduceti o bancnota [5 lei, 10 lei]"))
print(optiune)
if optiune == "1":
    rezultat = bancnota - cappucino
elif optiune == "2":
    rezultat = bancnota - espresso
else:
    rezultat = ("ti-am furat banii")
print(f"vei primi restul de {rezultat}")

a = int(input('ce optiune alegeti?') [1,2]'))
while not(1<=a<3):
    a=int(input('optiune invalida, alegeti optiune dintre 1 si 2'))




