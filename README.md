# Pipeline de dados

Neste projeto foi abordado a seguinte situação: Duas empresas se unificaram e agora precisam dos dados da empresaA e empresaB unidos. Porém, esses dados não estão no formato esperado e por isso foi criado este pipeline para extrair, tratar e carregar os dados. O famoso ETL.

## Criação das pastas da pipeline em um WSL

Esse processo foi crucial para colocarmos em pauta onde serão alocados as pastas e arquivos que estaremos trabalhando. Dessa forma, foi pensando em colocar em WSL (Windows Subsystem for Linux). Que é um subsistema do Linux no Windows onde estarei manipulando estes arquivos e criando pastas para organizar todo o projeto.

## Rodando o VSCode no nosso ambiente virtual

Na imagem abaixo, estamos chamando o 'dir' para listarmos as pastas criadas nesse caminho. Como já temos uma pasta "Documentos" criada, onde ficará os arquivos do nosso projeto, não será necessário utilizar o comando 'mkdir' para a criação da pasta para alocar os nosso arquivos.

![image](https://github.com/user-attachments/assets/bba89692-90c4-4d9b-bb83-ccd61e95be11)

## Explorando os dados no Jupyter Notebook

Após montarmos o ambiente e construir as pastas no diretório informado, realizamos a exploração dos dados com o Jupyter Notebook e assim fazemos toda a análise dos dados que estão sendo coletados nos arquivos .JSON e .CSV. Verificamos ali a quantidade de linhas em cada arquivo, cada Header (cabeçalho) dos arquivos e imprimindo os dados que contém neles.

Como o tipo do arquivo .CSV é um tipo lista nós precisamos deixar os arquivo .JSON neste mesmo padrão para que conseguissemos unir estes dados. Com isso, foi feito todo tratamento dos dados .JSON, assim como a nomenclatura das colunas para unificarmos esses dados. Na variável KeyMapping, foi possível fazer um de para das chaves que estavam listadas no arquivo, para que ficasse igual ao nosso .CSV.

Há um ponto se frisar, que nos nossos dados do arquivo .JSON não temos a chave 'Data da venda' como temos no arquivo .CSV. Porém, iremos incluir essa chave dentro do nosso arquivo de fusão e substituindo os valores em branco pela palavra "Indisponivel" para que assim possa ser demonstrado que essa coluna receberá os dados futuramente pelo departamento responsável.

![image](https://github.com/user-attachments/assets/6618ea7d-0f35-4e5b-a62b-7adeb0182b3e)

## Montando o nosso Script

### Script das fusões dos dados

Explorando os dados e entendendo como eles se comportam no nosso Notebook, agora está na hora de criarmos o nosso Script para os outros tratamentos que iremos realizar futuramente. Nesta primeira etapa já estamos fazendo a extração dos dados de ambos os arquivos, renomeando as nossas colunas e unindo estes dados. Importamos a nossso "processamento_dados" e atribuíndo a classe "dados" em nosso arquivo principal para que possamos classificarmos por metódos e atributos.

![image](https://github.com/user-attachments/assets/9cac1ac3-bc2e-4cc1-82f8-52e32c1a24b0)


### Sript do processamento dos dados

Nesta parte, estaremos classificando todo o tratamento dos dados dos dois arquivos pelo processo de atributos nesse método privado explícito em nosso código. Dentro dessa classe "dados" temos várias funções fazendo esse processamento. Uma delas é o tratamento das colunas com o List Comprehension que é muito utilizado para diminuir o tamanho do código que poderia ser utilizado, para ser mais eficiente que um for, por exemplo.

Após criarmos toda essa leitura e tratamento dos dados, iremos unir lá no final do código e salvar estes dados lá na última função criada dentro dessa classe. Isso está demonstrado na imagem 2 desse projeto. Assim, finalizando todo o tratamento dos dados e salvando em uma pasta chamada "data_processed". Esse arquivo ficará no tipo .CSV mesmo, como se trata de uma lista.

### Imagem 1:

![image](https://github.com/user-attachments/assets/ca1a339b-9f1a-4cdd-8071-ee2a318a6234)

### Imagem 2:

![image](https://github.com/user-attachments/assets/69faf4b2-92b0-43b8-b91a-c179e59f0230)

