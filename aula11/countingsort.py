import random

#========== Prefacio =====================

#Vimos que o Mergesort, Heapsort e Timsort tem complexidade de 
# pior caso O(n lg n)

#Vimos que o Quicksort (aleatorizado) tem tempo esperado O(n lg n) 
# para qualquer entrada, e na pratica Ã© muito rapido

#Provamos que qualquer algoritmo baseado em comparaÃ§Ãµes terÃ¡ 
# complexidade de pior caso pior que O(n lg n) (formalmente 
# dizemos que o algoritmo Ã© Omega(n lg n))

# ========= CountingSort =================

#CountingSort assume uma entrada de n inteiros no intervalo 
# de 0 atÃ© k. Roda em tempo O(n + k). EntÃ£o se k = O(n) o 
# countingsort roda em tempo O(n)

#queremos um vetor C[0:k] em que C[i] tem quantos elementos sÃ£o 
# menores ou iguais a i.

#Dessa forma dado um elemento a do vetor original sabemos que devemos 
# coloca-lo na posiÃ§Ã£o C[a] - 1.

#Para lidar com repetiÃ§Ãµes cada vez que inserimos um elemento na
#posiÃ§Ã£o C[a], podemos decrementar esse valor para que o prÃ³ximo
#a seja colocado numa posicao vazia C[a] -= 1

# ==========OrdenaÃ§Ã£o estÃ¡vel ===============
# uma ordenaÃ§Ã£o Ã© dita estÃ¡vel se ela preserva a ordem relativa
# de elementos "Iguais" (iguais aqui significam que elas tem a
# mesma chave

# O counting sort pode ser implmentado para ser uma ordenaÃ§Ã£o estÃ¡vel
# para isso vamos percorrendo o vetor A do final para o comeÃ§o.

def CountingSort(A, k):
  B = [None for _ in range(0, len(A))]
  C = [0 for _ in range(0, k+1)]
  for a in A:
    C[a] += 1
  for i in range(1, k+1):
    C[i] = C[i] + C[i-1]
  for i in range(len(A)-1, -1, -1):
    a = A[i]
    B[C[a] - 1] = a 
    C[a] -= 1 
  return B


#O quicksort aleatÃ³rizado era atÃ© entÃ£o o nosso algoritmo mais rapido
# colocamos ele e o insertionsort aqui para testar
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

def insertion_sort(lista):
  for i in range(1, len(lista)):
    j = i
    valor = lista[j]
    while j > 0 and lista[j-1] > valor:
      #lista[j-1] precisa ir pra direita
      lista[j] = lista[j-1]
      j = j - 1
    lista[j] = valor
    


#uma lista pequena para teste
k = 5
A = [2, 5, 4, 5, 1, 2, 2, 4, 3, 0]
B = CountingSort(A, k)

#uma lista grandona
k = 1_000_000
n = 10_000_000
A = [random.randint(0, k) for _ in range(0, n)]
  
B = CountingSort(A, k)  
#quicksort(A, 0, n-1)

 
  
  
  
  
  
  
  
  
  
