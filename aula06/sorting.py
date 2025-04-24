#Invariante de laÃ§o
#ApÃ³s a i-Ã©sima iteraÃ§Ã£o externa, os Ãºltimos i elementos do array estÃ£o ordenados e em suas posiÃ§Ãµes finais.
def bubble_sort(lista):
  k = len(lista) - 1
  for i in range(k, 0, -1):
    trocou = False
    for j in range(0, i, 1):
      if lista[j] > lista[j+1]:
        #estÃ£o invertidos
        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux
        trocou = True
    if trocou == False:
      return
        
#Invariante de laÃ§o
#No inÃ­cio da i-Ã©sima iteraÃ§Ã£o, os primeiros i elementos do array sÃ£o os originais e estÃ£o ordenados.
def insertion_sort(lista):
  for i in range(1, len(lista)):
    j = i
    valor = lista[j]
    while j > 0 and lista[j-1] > valor:
      #lista[j-1] precisa ir pra direita
      lista[j] = lista[j-1]
      j = j - 1
    lista[j] = valor



#Invariante de laÃ§o
#ApÃ³s a i-Ã©sima iteraÃ§Ã£o, os primeiros i elementos do array sÃ£o os menores do conjunto original e estÃ£o ordenados em suas posiÃ§Ãµes finais.
def selection_sort(lista):
  for i in range(len(lista)):
    #quero colocar o menor elemento
    #de lista[i:-1] na posiÃ§Ã£o i
    indice_menor = i
    for j in range(i+1, len(lista)):
      if lista[j] < lista[indice_menor]:
        indice_menor = j
    aux = lista[i]
    lista[i] = lista[indice_menor]
    lista[indice_menor] = aux



lista = [18, 1, 20, 6, 5, 30, 10, 6]
selection_sort(lista)
print(lista)