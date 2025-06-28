import csv 

# Função para converter uma string percentual ('52.3%') em float (52.3)
def parse_percent(value):
    return float(value.strip('%'))

# Função para converter uma string para float diretamente
def parse_float(value):
    return float(value)

# Função para carregar os dados de um arquivo CSV e processá-los
def carregar_dados(caminho_arquivo):
    dados = [] 
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)  
        cabecalho = next(leitor) 
        #dados.append(cabecalho) se quiser manter o cabeçalho

        for linha in leitor:
            nome = linha[0]  # Nome do campeão
            roles = [r.strip() for r in linha[1].split(',')]  # Lista de posições (ex: ['Mid', 'Top'])
            pickrate = parse_percent(linha[2])  # Taxa de escolha convertida para float
            winrate = parse_percent(linha[3])   # Taxa de vitória convertida para float
            banrate = parse_percent(linha[4])   # Taxa de banimento convertida para float
            kills = parse_float(linha[5])       # Média de abates
            deaths = parse_float(linha[6])      # Média de mortes
            assists = parse_float(linha[7])     # Média de assistências
            pentakills = parse_float(linha[8])  # Número de pentakills

            dados.append([nome, roles, pickrate, winrate, banrate, kills, deaths, assists, pentakills])
    return dados  

# Função auxiliar do radix sort: ordena os elementos com base em um dígito específico (representado pelo expoente)
def counting_sort_digito(lista, expoente):

    # Número de elementos na lista
    n = len(lista)  
    output = [0] * n

    # Lista para contagem dos digitos de 0 a 9
    count = [0] * 10

    # Conta as ocorrências de cada dígito (em ordem decrescente para ordenação reversa)
    for i in range(n):
        
        # Obtém o dígito relevante
        index = (lista[i][0] // expoente) % 10 

        # Incrementa a contagem no índice invertido
        count[9 - index] += 1  

    # Transforma a contagem em contagem acumulada (prefix sum)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Constrói a lista de saída usando a contagem acumulada
    for i in range(n - 1, -1, -1):
        index = (lista[i][0] // expoente) % 10
        output[count[9 - index] - 1] = lista[i]

        # Decrementa a contagem para o próximo item igual garantindo a ordenação estavel
        count[9 - index] -= 1  

    return output 

# Função principal de ordenação (Radix Sort adaptado para ordem decrescente)
def radix_sort(lista):

    # Retorna lista vazia se não houver nada para ordenar
    if not lista:
        return lista  

    # Encontra o maior valor na lista (para saber quantos dígitos ele tem)
    max_num = lista[0][0]
    for i in lista:
        if i[0] > max_num:
            max_num = i[0]

    # Expoente representa a posição do dígito (1 = unidades, 10 = dezenas, etc.)
    expoente = 1  

    while max_num // expoente > 0:
        # Expoente representa a posição do dígito (1 = unidades, 10 = dezenas, etc.)
        lista = counting_sort_digito(lista, expoente)

        # Passa para o próximo dígito (mais significativo) 
        expoente *= 10  

    return lista

if __name__ == "__main__":

    dados = carregar_dados('champs.csv')

    valores = [] 
    for linha in dados:
        # Calcula o KDA normalizado multiplicado por 1000 para se tornar um inteiro
        valores.append([int(round((linha[5] + linha[7]) / linha[6], 3) * 1000), linha[0]])

    # Ordena os valores usando radix sort
    valores = radix_sort(valores)

    for i in valores:
        print(i[1])
        