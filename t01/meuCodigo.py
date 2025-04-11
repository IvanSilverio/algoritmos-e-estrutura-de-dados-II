#Parte A

#No da arvore
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#Arvore Binaria de Busca
class Tree:
    def __init__(self):
        self.root = None

    #Insercao de valores na arvore
    def _insert(self, key, value):

        node = Node(key, value)
        #se o primeiro no esta vazio colocamos o primeiro item na lista e 
        #retornamos a arvore
        if self.root is None:
            self.root = node
            return self.root
        #Ja temos o primeiro item! Entao vamos compara-lo com o proximo 
        #para decidir se ele vai para o lado esquerdo ou direito
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                #se a chave que queremos inserir for maior que a anterior
                #iremos colocar ela no lado direito
                if node.key > parent.key:
                    current = current.right
                    #se o atual for igual a nada signfica que nao existe um 
                    #no nessa posicao, logo podemos armazenar 
                    if current is None:
                        parent.right = node
                        return self.root
                #A chave que queremos inserir eh menor que a anterior, logo
                #iremos colocar ela do lado esquerdo
                else:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return self.root
    
    #metodologia de printar a arvore na ordem (<raiz>, <subárvore esquerda>, <subárvore direita>)
    def _preorder(self, root):
        current = root
        #se o atual for igual a none nao ha oque printar logo matamos a funcao
        if current is None:
            return
        print(current.key, current.value)
        #chamamos sempre primeiro a recursao para a subarvore esquerda
        self.preorder(current.left)
        self.preorder(current.right)

    def _search(self, key):
        current = self.root
        while True:
            if current is None:
                print('{}\nNão encontrado'.format(key))
                return None
            elif current.key == key:
                print('Item encontrado', key)
                return key
            elif current.key > key:
                current = current.left
            else:
                current = current.right

#Tabela Hash
class HashTable:
    def __init__(self):
        self.size = 29
        self.slots = [None for i in range(self.size)]
        self.nodes = [None for i in range(self.size)]
        #para todas as posicoes nos iremos ter uma arvore binaria de busca
        for i in range(self.size):
            self.slots[i] = Tree()

    #Responsavel por calcular a posicao na tabela hash   
    def _hash(self, key):
        hash = 0
        mult = 1
        for i in key:
            hash += mult * ord(i)
            mult += 1
        
        return hash % self.size

    def _put(self, key, value):
        hash = self._hash(key)
        node = self.slots[hash]._insert(key, value)
        self.nodes[hash] = node

    def _get(self, key):
        hash = self._hash(key)
        self.slots[hash]._search(key)
    
    def _print(self):
        for i in range(self.size):
            self._preorder(self.nodes[i])

if __name__ == '__main__':
    #Abrimos o arquivo com as informações de craft
    with open("craft.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    currentItem = [[] for i in range(122)] 
    currentKey = [[] for i in range(122)] 
    count = 0
    addKey = True

    for line in file:
        #Se o conteudo de uma linha for somente um enter (\n) pulamos
        #para a proxima posicao da lista
        if line == '\n':
            count += 1
            addKey = True #prepara paga guardar a key, que estará na proxima linha
            
        #Utiliza-se o else para que nao armazenemos um espaco vazio na lista
        else:
            if addKey == True:
                currentKey[count].append(line.strip())
                addKey = False
            #line.strip() funcao que remove os \n das frases para nao os armazenarmos
            else:
                currentItem[count].append(line.strip()) #apenda como value na posição count

    file.close()
    print (currentKey[121])
    print(currentItem[121][0:])

  #ainda esta com problema e incompleto, apenas a ideia
    Table = HashTable()
    for i in range(len(file)):
        Table._put(currentKey[i], currentItem[i])

    for i in range (29):
        Table._print()
        


    #Inserir os valores na tabela hash
    # Table = HashTable()
    # for i in range(len(currentItem)):
    #     #Para o parametro key, passamo sempre a primeira casa do array
    #     #Agora para os valores inserimos todos os itens a partir da segunda casa
    #     Table._put(currentItem[i][0], currentItem[i][1:])

    # #Loop para acesso das informacoes da tabela hash
    # text = str(input())
    # while text != 'g':
    #     if text[0] == 'r':
    #         Table._get(text[2:])
    #     elif text[:3] == 'p r':
    #         Table._print()
    #     elif text[0] == 'i':
    #         print('second hashTable')
    #     elif text[:3] == 'p i':
    #         print('second hashtable')

    #     text = str(input)
    

