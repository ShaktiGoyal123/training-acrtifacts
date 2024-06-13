lista = ['a','b','c','d','e']
count = 0
for l in lista:
    #print('Index:', count,' Value:', l)
    count+=1

lista = ['a','b','c','d','e']
for count, l in enumerate(lista):
    print('Index:', count,' Value:', l)