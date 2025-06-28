substituicao ={
	'a': ['4', '@'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['5', '$'],
    'h': ['#'],
    'k': ['<', 'x']
}

def nome_generalizado(nome):
	nome = nome.lower()
	for char, characteres_equivalente in substituicao.items():
		for char_equivalente_atual in characteres_equivalente:
			nome = nome.replace(char_equivalente_atual, char)
	return nome

class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [[] for i in range(size)]
		
	def hash(self, s):
		mult = 0
		hash_value = 0
		for c in s[:3]:
			c = c.lower()
			hash_value += (123**mult) * ord(c)
			mult += 1
		return hash_value
		
	def put(self, key):
		geral = nome_generalizado(key)
		hv = self.hash(geral) % self.size
		#supor que todo put Ã© diferente
		self.slots[hv].append((key))

    #devolver uma lista de valores com as tres primeiras letras similares
	def get(self, key):
		geral = nome_generalizado(key)
		resultados = []
		hv = self.hash(geral) % self.size
		
		for k in self.slots[hv]:
			k_geral = nome_generalizado(k)            
			if k_geral[:3] == geral[:3]:
				resultados.append(k)
		return resultados

Table = HashTable(997)

nomes_invocadores = []
with open("invocadores.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome = linha.strip()  # Remove espaÃ§os em branco e quebras de linha
        if nome:  # Garante que nÃ£o adiciona linhas vazias
            Table.put(nome)

nome_busca = input()
while nome_busca != "-1":
    resultado = Table.get(nome_busca)
    if resultado:
        for i in range(len(resultado)):	
            print(f"Nome encontrado: {resultado[i]}")
    else:
            print("Nome nÃ£o encontrado.")
    nome_busca = input()
