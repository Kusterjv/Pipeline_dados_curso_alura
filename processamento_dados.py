import csv
import json

class dados:
    
    #criando os atributos dentro desse método privado desta classe dados
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()
        
     #criando a função de leitura dos dados json
    def leitura_json(self):
        dados_Json = []
        with open(self.path, 'r') as file:
            dados_Json = json.load(file)
            
        return dados_Json

    #criando a função de leitura dos dados csv
    def leitura_csv(self):
        dados_csv2 = []
        with open (self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv2.append(row)
                
            return dados_csv2

    #unindo os dados de cada função criada acima
    def leitura_dados(self):
        dados = []
        
        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
            
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
            
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
            
        return dados        
    
    #pegando as colunas dos últimos dados
    def get_columns(self):
        
        return list(self.dados[-1].keys())
    
    #tratando as colunas através do list comprehension
    def rename_columns(self, key_mapping):
        new_dados = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
    
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
        
    #verificando a quantidade destes dados
    def size_data(self):
        
        return len(self.dados)

    #combinando os dados
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return dados(combined_list, 'list')
    
    #transformando os dados em listas
    def transformando_dados_tabela(self):
        
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha  = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
            
        return dados_combinados_tabela
    
    #salvando os dados tipo lista
    def salvando_dados(self, path):
        
        dados_combinados_tabela = self.transformando_dados_tabela()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)