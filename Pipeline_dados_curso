import json
import csv

#criando a função de leitura dos dados json
def leitura_json(path_json):
    dados_Json = []
    with open(path_json, 'r') as file:
        dados_Json = json.load(file)
    return dados_Json

#criando a função de leitura dos dados csv
def leitura_csv(path_csv):
    dados_csv2 = []
    with open (path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv2.append(row)
        return dados_csv2

#unindo os dados de cada função criada acima
def leitura_dados(path, tipo_arquivo):
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
        
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
        
    return dados

#pegando as colunas dos últimos dados
def get_columns(dados):
   return list(dados[-1].keys())

#tratando as colunas através do list comprehenshion
def rename_columns(dados, key_mapping):
    new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados]
    new_dados_csv[0]
    
    return new_dados_csv

#verificando a quantidade destes dados
def size_data(dados):
    return len(dados)

#combinando os dados
def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

#transformando os dados em listas
def transformando_dados_tabela(dados, nome_colunas):
    dados_combinados_tabela = [nome_colunas]

    for row in dados:
        linha  = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

#salvando os dados tipo lista
def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)
    

#buscando os dados em seus diretórios 
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#iniciando a leitura dos dados em json
dados_Json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_Json)
tamanho_json = size_data(dados_Json)
print(f"Colunas Json: {nome_colunas_json}")
print(f"Quantidade de dados Json: {tamanho_json}")

#iniciando a leitura dos dados em csv
dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_csv = size_data(dados_csv)
print(f"Colunas CSV: {nome_colunas_csv}")
print(f"Quantidade de dados CSV: {tamanho_csv}")

#transformação das chaves da lista
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Quantidade em Estoque',
               'Data da Venda': 'Data da Venda'
               }

#combinando as novas chaves com os dados csv
dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"Novas colunas CSV: {nome_colunas_csv}")

#criando a fusão dos dados json e csv e retornando o nome dessas colunas junto com a quantidade de dados
dados_fusao = join(dados_Json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_fusao = size_data(dados_fusao)
print(f"Colunas fusão: {nome_colunas_fusao}")
print(f"Quantidade de dados fusão: {tamanho_fusao}")


#salvando os dados das fusões na variável
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

#direcionando onde será salvo esses dados
path_dados_combinados = 'data_processed/dados_combinados.csv'

#passando o parâmetro de salvamento deste dados
salvando_dados(dados_fusao_tabela, path_dados_combinados)

#printando os dados salvos no diretório informado no nosso path
print(path_dados_combinados)
