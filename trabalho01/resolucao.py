#No da arvore
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.values = []
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
            self.root.values.append(value)
            return self.root
        #Ja temos o primeiro item! Entao vamos compara-lo com o proximo 
        #para decidir se ele vai para o lado esquerdo ou direito
        else:
            current = self.root
            parent = None
            while True:
                parent = current

                if current.key == key:
                    current.values.append(value)
                    return self.root
                
                #se a chave que queremos inserir for maior que a anterior
                #iremos colocar ela no lado direito
                if node.key > parent.key:
                    current = current.right
                    #se o atual for igual a nada signfica que nao existe um 
                    #no nessa posicao, logo podemos armazenar 

                    if current is None:
                        parent.right = node
                        node.values.append(value)
                        return self.root
                    
                #A chave que queremos inserir eh menor que a anterior, logo
                #iremos colocar ela do lado esquerdo
                else:
                    current = current.left
                    if current is None:
                        parent.left = node
                        node.values.append(value)
                        return self.root
    
    #metodologia de printar a arvore na ordem (<raiz>, <subárvore esquerda>, <subárvore direita>)
    def _preorder(self, root):
        current = root
        #se o atual for igual a none nao ha oque printar logo matamos a funcao
        if current is None:
            print('None', end = '')
            return 
        print(f'({current.key}, ', end = '')
        #chamamos sempre primeiro a recursao para a subarvore esquerda
        self._preorder(current.left)
        print(', ', end='')
        self._preorder(current.right)
        print(')', end = '')

    def _search(self, key):
        current = self.root
        while True:
            if current is None:
                print('{}\nNão encontrado'.format(key))
                return None
            elif current.key == key:
                print('{}'.format(current.key))
                for i in range(len(current.values)):
                    print('{}'.format(current.values[i]))
                return
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
            self.slots[i]._preorder(self.nodes[i])
            print()

if __name__ == '__main__':
    # Falta ajeitar a quebra de linha
    # Leitura do arquivo
    # Abrimos o arquivo com as informações de craft
    def nonumbers(string):
        nonumbers = []
        for i in string:
            if not i.isdigit():
                nonumbers.append(i)
            
        return ''.join(nonumbers)
    
    with open("craft.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    #Lista que vai armazenar os itens e seus ingredientes
    #Parte A
    currentItem = [[] for i in range(122)]
    #Parte B
    currentIngredients = [[] for i in range(122)]
    count = 0
    
    for line in lines:
        #Se o conteudo de uma linha for somente um enter (\n) pulamos
        #para a proxima posicao da lista
        if line == '\n':
            count += 1
        #Utiliza-se o else para que nao armazenemos um espaco vazio na lista
        else:
            #Parte B retira os numeros dos ingredientes para adicionar na arvore
            line2 = nonumbers(line)
            #line.strip() funcao que remove os \n das frases para nao os armazenarmos
            #Parte B 
            currentIngredients[count].append(line2.strip())
            #Parte A
            currentItem[count].append(line.strip())

    file.close()
    #Inserir os valores na tabela hash
    #Parte A
    Table = HashTable()
    #Parte B
    TableItems = HashTable()
    for i in range(len(currentIngredients)):
        #Para a arvore de itens começamos desde o inicio e passamos todos os valores 
        for j in range(1, len(currentIngredients[i])):
            Table._put(currentItem[i][0], currentItem[i][j])
            TableItems._put(currentIngredients[i][j], currentIngredients[i][0])
            # Debug print(currentItem[i][0])
            # Debug print(currentItem[i][j])
        
    #Loop para acesso das informacoes da tabela hash
    text = str(input())
    while text != 'q':
        if text[0] == 'r':
            Table._get(text[2:])
        elif text[:3] == 'p r':
            Table._print()
        elif text[0] == 'i':
            TableItems._get(text[2:])
        elif text[:3] == 'p i':
            TableItems._print()

        text = str(input())

# Com a profissão Armadilheiro: Madeira 25
# erro na craft
