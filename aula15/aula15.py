class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[] for _ in range(size)]

    def corrigeValor(self, c):
        nameDict = {
            '4': 'a', '@': 'a',
            '3': 'e',
            '1': 'i', '!': 'i',
            '0': 'o',
            '5': 's', '$': 's',
            '#': 'h',
            '<': 'k', 'x': 'k'
        }
        return ord(nameDict[c])

    def hash(self, s):
        mult = 0
        hash_value = 0
        for c in s[:3]:
            c = c.lower()
            if c in ['4', '@', '3', '1', '!', '0', '5', '$', '#', '<', 'x']:
                val = self.corrigeValor(c)
            else:
                val = ord(c)
            hash_value += (123 ** mult) * val
            mult += 1
        return hash_value

    def put(self, key):
        hv = self.hash(key) % self.size
        self.slots[hv].append(key)

    def get(self, key):
        resultado = []
        hv = self.hash(key) % self.size
        valueKey = self.hash(key)
        
        for k in self.slots[hv]:
            valueK = self.hash(k)
                
            if valueKey == valueK:
                resultado.append(k)
        return resultado


# Inicializa a tabela
Table = HashTable(997)

# Lê os nomes do arquivo
with open("invocadores.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome = linha.strip()  # Remove espaços em branco e quebras de linha
        if nome:
            Table.put(nome)

# Busca por nomes
nome_busca = input()

while nome_busca != "-1":
    resultado = Table.get(nome_busca)
    if resultado:
        print(f"Nome encontrado: {resultado}")
    else:
        print("Nome não encontrado.")
    nome_busca = input()
