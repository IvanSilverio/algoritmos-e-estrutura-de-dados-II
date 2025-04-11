#Em python as variÃ¡veis tem tipos, mas nÃ£o precisamos declarar explicitamente
x = 10
y = "nome"
z = 100.0
c = 10 + 5j
print(type(x))
print(type(y))
print(type(z))
print(type(c))

#podemos inclusive substituir o valor de uma variÃ¡vel com outro tipo
x = "sobrenome"
print(type(x))

#outro tipo Ã© o booleano
b1 = True
b2 = False
print(type(b1))
print(type(b2))

#a funÃ§Ã£o bool() pode receber um valor numÃ©rico e devolve
# True se o nÃºmero for diferente de zero
# False apenas se o valor for zero 
print(bool(z))
z = 0.000000000000000000000005
print(z)
print(bool(z))

#Cuidado! Quando trabalhando com nÃºmeros do tipo ponto flutuante
#em qualquer linguagem Ã© preciso se preocupar com a precisÃ£o da variÃ¡vel
#por exemplo, adicionamos 1 e subtratimos 1, matemÃ¡ticamente z deveria ter
#mantido o valor. PorÃ©m como 1000000000000000000000005 Ã© uma mantissa maior
#do que a aceita pela linguagem ele acaba perdendo o 5 do final
#de tal forma que agora z Ã© zero. Verifique abaixo.
z = z + 1
z = z - 1
print(z)
print(bool(z))


#Tipos sequenciais
#============= Strigs ===================#
#Strings sÃ£o um tipo de dado bÃ¡sico e sequencial de python 
#podemos usar aspas simples, duplas, ou tres aspas simples (para strings 
# com multiplas linhas).

str1 = 'Hokama'
str2 = "STCO02"
str3 = """String com
varias linhas"""

#podemos fazer algumas operaÃ§Ãµes com strings
str4 = str1 * 3
str5 = str1 + " " + str2
print(str4)
print(str5)


#=============== Listas ===================#
#Listas sÃ£o array dinamicos que guardam referÃªncias para objetos
#que podem ser de qualquer tipos, inclusive misturar objetos de tipos
#diferentes.
lista1 = [1, 2, 3, 4]
lista2 = ["Hokama", "Stco02"]
lista3 = [1, 'SIN', 2, "hokama", lista1]

print(lista3) 


#Alguns objetos sÃ£o imutÃ¡veis como tipos numÃ©ricos, boleanos e strings
#Outros sÃ£o mutÃ¡veis como as listas. 
#Quando definimos uma funÃ§Ã£o alguns tipos sÃ£o passados "por valor" e outros
#sÃ£o passados "por referÃªncia" (as aspas sÃ£o pq estou usando a terminologia 
#que usamos em c para facilitar)
def foo(x):
	x = x + 1
	return
	
def foo2(l):
	l[0] = l[0] + 1
	return

#por exemplo, considerendo as duas funÃ§Ãµes acima, o que serÃ¡ impresso? 1 ou 2?
x = 1
foo(x)
print(x)

#E aqui, o que serÃ¡ impresso [1, 2, 3, 4] ou [2, 2, 3, 4]?
l = [1, 2, 3, 4]
foo2(l)
print(l)

#str1 e str2 "apontam" para o mesmo lugar na memÃ³ria onde tem o valor BANANA escrito
str1 = "BANANA"
str2 = str1
print(str2)
print(id(str1))
print(id(str2))

#quando fazermos a linha abaixo str2.lower() necessÃ¡riamente cria uma nova string
#(lembre que string sÃ£o imutÃ¡veis) e fazemos str2 "apontar" para essa nova string
str2 = str2.lower()
print(str1)


lista1 = ["B", "A",  "N"]
lista2 = lista1
#Nesse ponto lista2 e lista1 sÃ£o a MESMA lista portanto mudando uma, mudamos a outra
lista2[0] = 'b'
print(lista1)

#Outro tipo sequencial Ã© o range. Mas ele nÃ£o aloca explicitamente todos os valores
#isso Ã© importÃ¢nte para o desempenho do programa
for i in range(0,10,1):
	print(i)


# Range Ã© mais eficiente do que fazer uma lista com os mesmos nÃºmeros e percorre-la
#compare o desenpenho dos cÃ³didos abaixo

x = 0
for i in range(0,10_000_000,1):
	x = x + i
	
x = 0
lista1 = list(range(0,10_000_000,1))
for i in lista1:
	x = x + i

#Podemos acessar elementos de uma lista com colchetes igual a c
#ou ainda podemos acessar do fim para o comeÃ§o usando nÃºmeros
#negativos
lista1 = [1, 2, 3, 4]
print(lista1[1])
print(lista1[-1])

#podemos copiar um trecho de uma lista delimitanto os indices que queremos 
#(exclusive o ultimo)
lista2 = lista1[1:3]
print(lista2)
lista2 = lista1[1:-1]
print(lista2)


#note que lista 2 Ã© outra lista. os valores foram copiados
lista2[0] = 100
print(lista1)
print()
print()
print()



lista1 = [1, 2, 3, 4]

#note que os dois trechos de codigos tem o mesmo efeito visual
#1)
lista2 = lista1
print(lista2)

#2)
lista2 = lista1[0:]
print(lista2)

#entretanto os trechos 1 e 2 sÃ£o bem diferente, enquanto em 1 as duas sÃ£o a mesma lista
#em 2 as duas lista sÃ£o cÃ³pias identicas.

print(lista1)
print(lista2)
print(id(lista1))
print(id(lista2))

#==== OperaÃ§Ãµes em lista ====
#Podemos usar algumas operaÃ§Ãµes Ãºteis em python, por exemplo "in" e "not in"
#para verificarmos se um valor estÃ¡ na lista
print(2 in lista1)
print(1 not in lista1)


