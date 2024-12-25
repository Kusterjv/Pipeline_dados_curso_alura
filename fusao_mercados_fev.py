from processamento_dados import dados

#buscando os dados em seus diretórios 
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


#Extração dos dados entre ambos os arquivos
dados_empresaA = dados(path_json, 'json')
print(f"Colunas JSON: {dados_empresaA.nome_colunas}")
print(f"Quantidade de linhas do arquivo JSON: {dados_empresaA.qtd_linhas}")

dados_empresaB = dados(path_csv, 'csv')
print(f"Colunas CSV: {dados_empresaB.nome_colunas}")
print(f"Quantidade de linhas do arquivo CSV: {dados_empresaB.qtd_linhas}")

#transformação das keys
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Quantidade em Estoque',
               'Data da Venda': 'Data da Venda'
               }

#renomeando as colunas
dados_empresaB.rename_columns(key_mapping)
print(f"Colunas ajustadas: {dados_empresaB.nome_colunas}")

#unindo so dados através do método join aplicado na classe dados
dados_fusao = dados.join(dados_empresaA, dados_empresaB)
print(f"Colunas fusão: {dados_fusao.nome_colunas}")
print(f"Quantidade de linhas do arquivo de fusão: {dados_fusao.qtd_linhas}")

#carregamento dos dados

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Caminho dos dados unidos: {path_dados_combinados}")
