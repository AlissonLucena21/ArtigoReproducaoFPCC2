import csv

# Definir os índices das colunas a serem removidas (baseados em zero)
indices_colunas_a_remover = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
 
# Nome dos arquivos CSV de entrada
arquivos_csv = ['Trepn_Rec_Room_2023.07.06_082629 - TESTE 1.csv',
                'Trepn_Rec_Room_2023.07.06_083425 - TESTE 2.csv',
                'Trepn_Rec_Room_2023.07.06_084015 - TESTE 3.csv',
                'Trepn_Rec_Room_2023.07.06_085630 - TESTE 4.csv',
                'Trepn_Rec_Room_2023.07.06_090033 - TESTE 5.csv',
                'Trepn_Rec_Room_2023.07.06_090801 - TESTE 6.csv',
                'Trepn_Rec_Room_2023.07.06_091206 - TESTE 7.csv',
                'Trepn_Rec_Room_2023.07.06_091652 - TESTE 8.csv',
                'Trepn_Rec_Room_2023.07.06_092140 - TESTE 9.csv',
                'Trepn_Rec_Room_2023.07.06_092755 - TESTE 10.csv']

# Nome do arquivo CSV de saída
arquivo_saida = 'Testes_TRAPN_REMOVIDO.csv'

# Obter o cabeçalho do primeiro arquivo CSV
with open(arquivos_csv[0], 'r') as entrada:
    leitor_csv = csv.reader(entrada)

    for _ in range(3):
        next(leitor_csv)
    
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
            linhas = list(csv.reader(entrada))
            
            # Remover as primeiras 4 linhas e as últimas 27 linhas
            linhas = linhas[4:-27]

            # Ler cada linha do arquivo de entrada, remover as colunas especificadas e adicionar a coluna "Teste", e escrever a linha no arquivo de saída
            for linha in linhas:
                nova_linha = [numero_teste] + [valor for indice, valor in enumerate(linha) if indice not in indices_colunas_a_remover]
                escritor_csv.writerow(nova_linha)

        numero_teste += 1  # Incrementa o número do teste a cada mudança de arquivo

print(f'Dados dos arquivos CSV foram juntados em {arquivo_saida} com a coluna "Teste" adicionada apenas uma vez, as colunas especificadas removidas e as quatro primeiras linhas e 26 últimas linhas vazias removidas!')
