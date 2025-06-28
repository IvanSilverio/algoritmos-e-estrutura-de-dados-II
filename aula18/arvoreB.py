#cada no, exceto a raiz, tem pelo menos t-1 chaves 
#e no mÃ¡ximo 2t-1 chaves e 2t filhos
t = 3

class node:
  def __init__(self):
    self.n = 0 
    self.folha = True
    self.chaves = []
    self.filhos = []

def imprime_arvore(raiz, nivel=0):
  for i in range(nivel):
    print("  ", end="")
  print(raiz.chaves)
  for filho in raiz.filhos:
    imprime_arvore(filho, nivel + 1)

def busca(x, k):
  i = 0
  while i < x.n and k > x.chaves[i]:
    i += 1
  if i < x.n and k == x.chaves[i]:
    return x.chaves[i]
  elif x.folha:
    return None
  else:
    #se tiver no disco 
    #le(x.filhos[i])
    return busca(x.filhos[i], k)

arvore = node()
arvore.chaves = [100, 200]
arvore.n = 2
arvore.folha = False
arvore.filhos = [node(), node(), node()]

arvore.filhos[0].folha = True
arvore.filhos[0].n = 5
arvore.filhos[0].chaves = [1, 6, 18, 33, 42]

arvore.filhos[1].folha = True
arvore.filhos[1].n = 3
arvore.filhos[1].chaves = [150, 175, 180]

arvore.filhos[2].folha = True
arvore.filhos[2].n = 2
arvore.filhos[2].chaves = [250, 275]

imprime_arvore(arvore)