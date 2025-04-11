lista1 = [1, 2, 3, 4]

#alÃ©m do "in" e "not in"
print(1 in lista1)
print(10 in lista1)
print(2 not in lista1)
print(20 not in lista1)

# Outras operaÃ§Ãµes jÃ¡ sÃ£o existente para listas como a contatenaÃ§Ã£o
lista2 = lista1 + [5, 6, 7]
lista2[0] = 100
print(lista2)

#note que a concatenacao cria uma copia da lista
print(lista1)

#Adicionar novos itens
lista2.append(200)
print(lista2)
print(id(lista2))

lista2.insert(1, 300)
print(lista2)
print(id(lista2))

lista2.extend(lista1)
print(lista2)
print(id(lista2))
#Note que o extend copia os itens da lista que Ã© passada como parametro
lista2[-1] = 1000
print(lista1)

lista2.extend((500,100))
print(lista2)
print(id(lista2))

#Note que Ã© diferente do comando abaixo
#lista2.append((500,100))
#print(lista2)
#print(id(lista2))


#descobrir o tamanho, o minimo e o mÃ¡ximo
print(len(lista2))
print(min(lista2))
print(max(lista2))



#Podemos verificar se duas listas sÃ£o iguais
lista3 = [1, 2, 3, 4]
if lista1 == lista3:
    print("Lista iguais")
else:
    print("Lista diferentes")

#Podemos verificas de duas lista ou dois objetos quaisquer
#sÃ£o o mesmo objeto
if lista1 is lista3:
    print("lista1 e lista3 sÃ£o o mesmo objeto")
else:
    print("lista1 e lista3 sÃ£o objetos distintos")

#Existe o "is not"
if lista1 is not lista3:
    print("lista1 e lista3 sÃ£o objetos distintos")
else:
    print("lista1 e lista3 sÃ£o o mesmo objeto")

#====== Operadores lÃ³gicos =========
if 1 < 2 and 3 >= 3 and not 5 > 6 or 7 < 3:
    print("passou no if")
    

#========= TUPLAS ===========
#as tuplas sÃ£o sequencias ordenadas de itens (assim como as tuplas da matematica)
#semelhantes as listas, porÃ©m elas sÃ£o imutÃ¡veis
tupla1 = ("Hokama", 10)
tupla2 = ("Hokama", 10)
print(id(tupla1))
print(id(tupla2))

#posso acessar os itens da tupla como uma lista
print(tupla1[1])
print(tupla1[-1])

#PorÃ©m nÃ£o posso alterar o valor da mesma forma
#tupla1[1] = 8

#outras operaÃ§Ãµes com tuplas
#len, contatenacao, slicing, repeticao, pertencimento, iteracao
print(len((4, 5, "hello")))
tupla3 = (4, 5) + (10, 20)
print(tupla3[1:])
print(tupla1[-1])
print((2,1)*3)
print(3 in ('hi', 'xyz',3))
for p in tupla1:
    print(p)

