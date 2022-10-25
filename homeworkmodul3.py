# ex4
 parola = 7788
 while True:
     password = int(input("spune-mi parola"))
     if parola == password:
         break
         print("parola gresita. mai incercati.")
 print("acces granted")


#ex5

 obiecte = ["Masa", 5, "Scaun", 4.5, [5,6,7],8]
 print("Tipul obiectului Masa este:", type(obiecte[0]))
 print("Tipul obiectului 5 este:", type(obiecte[1]))
 print("Tipul obiectului [5,6,7]este:", type(obiecte[4]))

ex6
 cuvant = input("spune-mi un cuvant")
 x = cuvant[0].lower()
 y = 0
 for i in cuvant:
     if x == i:
         y +=1
 print(x, "Apare de", y, "ori")






