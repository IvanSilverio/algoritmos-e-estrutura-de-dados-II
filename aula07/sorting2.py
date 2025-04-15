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


def quicksort(lista, esq, dir):
  if esq < dir:
    p = partition(lista, esq, dir)
    quicksort(lista, esq, p-1)
    quicksort(lista, p+1, dir)



listaA = [1, 18, 33, 42]
listaB = [2, 13, 16, 46]
lista = merge(listaA, listaB)
print(lista)


lista = [18, 1, 33, 42, 33, 42, 13]
lista = mergesort(lista)
print(lista)
