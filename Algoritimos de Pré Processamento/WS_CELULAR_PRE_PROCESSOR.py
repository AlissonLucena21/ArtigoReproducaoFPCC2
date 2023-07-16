import csv

# Definir os índices das colunas a serem removidas (baseados em zero)
indices_colunas_a_remover = [1, 4, 6, 7]

# Nome dos arquivos CSV de entrada
arquivos_csv = ['Teste 1_CELULAR_WS.csv',
                'Teste 2_CELULAR_WS.csv',
                'Teste 3_CELULAR_WS.csv',
                'Teste 4_CELULAR_WS.csv',
                'Teste 5_CELULAR_WS.csv',
                'Teste 6_CELULAR_WS.csv',
                'Teste 7_CELULAR_WS.csv',
                'Teste 8_CELULAR_WS.csv',
                'Teste 9_CELULAR_WS.csv',
                'Teste 10_CELULAR_WS.csv']

# Nome do arquivo CSV de saída
arquivo_saida = 'Testes_CELULAR_WS_REMOVIDO.csv'

# Obter o cabeçalho do primeiro arquivo CSV
with open(arquivos_csv[0], 'r') as entrada:
    leitor_csv = csv.reader(entrada)
    cabecalho = next(leitor_csv)

# Adicionar a coluna "Teste" ao cabeçalho
cabecalho = ['Teste'] + [valor for indice, valor in enumerate(cabecalho) if indice not in indices_colunas_a_remover]

# Abrir o arquivo CSV de saída para escrita
with open(arquivo_saida, 'w', newline='') as saida:
    escritor_csv = csv.writer(saida)

    # Escrever o cabeçalho no arquivo de saída apenas uma vez
    escritor_csv.writerow(cabecalho)

    # Iterar sobre os arquivos CSV de entrada
    numero_teste = 1  # Inicializa o número do teste como 1

    for arquivo_csv in arquivos_csv:
        with open(arquivo_csv, 'r') as entrada:
            leitor_csv = csv.reader(entrada)

            # Pular a primeira linha (cabeçalho) de todos os arquivos (o cebeçalho já foi inserido)
            next(leitor_csv)

            # Ler cada linha do arquivo de entrada, remover as colunas especificadas e adicionar a coluna "Teste", e escrever a linha no arquivo de saída
            for linha in leitor_csv:
                nova_linha = [numero_teste] + [valor for indice, valor in enumerate(linha) if indice not in indices_colunas_a_remover]
                escritor_csv.writerow(nova_linha)

        numero_teste += 1  # Incrementa o número do teste a cada mudança de arquivo

print(f'Dados dos arquivos CSV foram juntados em {arquivo_saida} com a coluna "Teste" adicionada apenas uma vez e as colunas especificadas removidas!')
