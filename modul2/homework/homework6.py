x = "a\nn\na\nn\na\ns\n"
print(x)


x = "Ananas"
print(x[0:3])
print(x[3:1])

print(x[0:2], x[2:5], x[5], sep=":")

print(x[0:3], x[3:5], x[5], sep="_")
print(x[1:3]*8)

cuvant = input("Spune un cuvant")
print("Sirul incepe cu majuscula", cuvant[0]==cuvant.upper()[0])
