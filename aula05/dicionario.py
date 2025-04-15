#JÃ¡ vimos os tipos bÃ¡sicos:
    #NumÃ©ricos: Inteiro, ponto flutuante, complexo
    #Booleanos
    #Sequencias: Strings, Listas, Tuplas

#Veremos os tipos complexos de dados
    #DicionÃ¡rios
    #Sets e Frozen Sets

#Um dicionÃ¡rio associa pares (chave - valor) 

dicio_girias = {
    "gg": "good game",
    "hs": "head shot",
    "fb": "first blood",
    "kda": "Kills Deaths Assists",
    "dronar": "Usar o drone do Sova"
}

print(dicio_girias["gg"])

dicio_girias["smokar"] = "Usar uma granada de fumaÃ§a"
dicio_girias["ns"] = "Nice Shot"
dicio_girias["pinar"] = "Errar todas as balas"

print(dicio_girias["ns"])
print(dicio_girias.get("ns"))

#Uma key pode ser qualquer objeto imutÃ¡vel e hashÃ¡vel
dicio_girias[1] = "nÃºmero 1"
dicio_girias[(1, 2)] = "tupla"

#lista nÃ£o Ã© imutÃ¡vel e nÃ£o Ã© hashÃ¡vel, nÃ£o pode
#dicio_girias[[1, 2]] = "lista"

#Uma tupla que contÃ©m uma ula lista Ã© imutÃ¡vel, mas nÃ£o Ã© hashÃ¡vel
#tambÃ©m nÃ£o pode
#dicio_girias[([1, 2], 3)] = "tupla"

print ("ns" in dicio_girias)
print ("dm" in dicio_girias)

print(dicio_girias)

#dicio_girias.items() devolve um iterador nos pares do dicionario
#print(dicio_girias.items())
for (k, v) in dicio_girias.items():
    print(f"{k}: {v}")

for k in dicio_girias.keys():
    print(k)

for k in dicio_girias.values():
    print(k)

print(dicio_girias.pop("ns"))
print("ns" in dicio_girias)

print(dicio_girias.popitem())

new_dicio = {"pinar": "hokama",
            "TR": "Terroristas", 
            "CT": "Contra-Terroristas"
}

dicio_girias.update(new_dicio)
for (k, v) in dicio_girias.items():
    print(f"{k}: {v}")

print(len(dicio_girias))
dicio_girias.clear()
print(len(dicio_girias))


#sets: conjuntos, como na matemÃ¡tica
#set Ã© uma coleÃ§Ã£o nÃ£o ordenada de objetos hashÃ¡veis (e portanto imutÃ¡veis)
#Ã© mutÃ¡vel e tem elementos Ãºnicos

s1 = {5, 4, 3, 2, 1}
s2 = set([2, 4, 6, 8, 10])

print(s1)

#set permitem algumas operaÃ§Ãµes
#in
print(1 in s1)
print(2 not in s2)

#uniÃ£o
print(s1 | s2)
print(s1.union(s2))
print(s1)

#interseÃ§Ã£o
print(s1 & s2)
print(s1.intersection(s2))

#diferenÃ§a
print(s1 - s2)
print(s1.difference(s2))
#lembrando que a diferenÃ§a nÃ£o Ã© simÃ©trica
print(s2 - s1)

#diferenÃ§a simÃ©trica
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

#contem
s3= {1, 2}
print(s1.issubset(s2))
print(s1 <= s2)

print(s1.issuperset(s2))
print(s1 >= s2)

print(s3.issubset(s1))
print(s3 <= s1)

print(s1.issuperset(s3))
print(s1 >= s3)

s3.add(3)
print(s3)
s3.remove(3)
s3.add(4)
print(s3)
#pop remove um elemento arbitrÃ¡rio
s3.pop()
print(s3)


#conjuntos imutÃ¡veis
f1 = frozenset([5, 4, 3, 2, 1])
f2 = frozenset([2, 4, 6, 8, 10])

print(f1 | f2)
print(f1 & f2)
#tudo que Ã© permitido em set Ã© permitido em frozenset
#exceto operaÃ§Ãµes que alteram o conjunto
#como add, remove, pop, clear
#f1.add(6) #erro

#namedtuple
#deque
#defaultdict
#ChainMap
#Counter
#UserDict