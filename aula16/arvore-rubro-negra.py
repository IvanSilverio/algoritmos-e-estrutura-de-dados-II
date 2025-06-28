class noh:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.cor = True
    
def rotacionaEsquerda(x):
  y = x.dir
  x.dir = y.esq
  y.esq = x
  y.cor = x.cor
  x.cor = True 
  return y

def rotacionaDireita(x):
  y = x.esq
  x.esq = y.dir
  y.dir = x
  y.cor = x.cor #sera que x eh sempre negro?
  x.cor = True
  return y
  
def sobeVermelho(x):
  x.cor = True
  x.esq.cor = False
  x.dir.cor = False
  return x

def ehVermelho(x):
  if x == None:
    return False
  return x.cor
  
def ehNegro(x):
  if x == None:
    return True
  return x.cor == False

#recebe uma arvore e devolve o endereÃ§o da nova arvore com o dado adicionado
def insere_aux(raiz, dado):
  if raiz == None:
    return noh(dado)
  elif dado < raiz.dado:
    raiz.esq = insere_aux(raiz.esq, dado)
  elif dado > raiz.dado:
    raiz.dir = insere_aux(raiz.dir, dado)
  else:
    return raiz
    
  #verificar se quebrou propriedades
  if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
    raiz = rotacionaEsquerda(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
    raiz = rotacionaDireita(raiz)
  if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
    sobeVermelho(raiz)
  return raiz
  
def insere(raiz, dado):
  raiz = insere_aux(raiz, dado)
  raiz.cor = False
  return raiz

def imprime(A):
  if A == None:
    return
  print('(', end='')
  imprime(A.esq)
  print(',', end='')
  print(A.dado, end=',')
  imprime(A.dir)
  print(')', end='')

A = None
A = insere(A, 7)
A = insere(A, 5)
A = insere(A, 9)
A = insere(A, 3)
A = insere(A, 1)
A = insere(A, 2)

imprime(A)
print()



