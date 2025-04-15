import sys

def merge(listaA, listaB):
  lista = []
  i = 0
  j = 0
  while i < len(listaA) and j < len(listaB):
    if listaA[i] < listaB[j]:
      lista.append(listaA[i])
      i += 1
    else:
      lista.append(listaB[j])
      j += 1
      
  while i < len(listaA):
    lista.append(listaA[i])
    i += 1
    
  while j < len(listaB):
    lista.append(listaB[j])
    j += 1
  return lista
    

def mergesort(lista):
  if len(lista) <= 1:
    return lista
    
  meio = len(lista) // 2    
  listaA = mergesort(lista[:meio])
  listaB = mergesort(lista[meio:])
  return merge(listaA, listaB)

import random

def partition(lista, esq, dir):
  r = random.randint(esq,dir)
  aux = lista[r]
  lista[r] = lista[esq]
  lista[esq] = aux
  j = esq
  pivot = lista[esq]
  for k in range(esq+1, dir + 1):
    if lista[k] < pivot:
      j += 1
      aux = lista[k]
      lista[k] = lista[j]
      lista[j] = aux
  lista[esq] = lista[j]
  lista[j] = pivot
  return j
  
      

def quicksort(lista, esq, dir):
  if esq < dir:
    p = partition(lista, esq, dir)
    quicksort(lista, esq, p-1)
    quicksort(lista, p+1, dir)  

sys.setrecursionlimit(100000)

lista = list(range(0, 15000))
quicksort(lista, 0, len(lista)-1)

print(lista)

