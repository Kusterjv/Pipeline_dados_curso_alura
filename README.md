# Pipeline de dados

Neste projeto foi abordado a seguinte situação: Duas empresas se unificaram e agora precisam dos dados da **empresaA** e **empresaB** unidos. Porém, esses dados não estão no formato esperado e por isso foi criado este pipeline para extrair, tratar e carregar os dados. O famoso ETL.

### Criação das pastas da pipeline em um WSL

Esse processo foi crucial para colocarmos em pauta onde serão alocados as pastas e arquivos que estaremos trabalhando. Dessa forma, foi pensando em colocar em WSL (**Windows Subsystem for Linux**). Que é um subsistema do Linux no Windows onde estarei manipulando estes arquivos e criando pastas para organizar todo o projeto.

### Rodando o VSCode no nosso ambiente virtual

Na imagem abaixo, estamos chamando o '**dir**' para listarmos as pastas criadas nesse caminho. Como já temos uma pasta "Documentos" criada, onde ficará os arquivos do nosso projeto, não será necessário utilizar o comando '**mkdir**' para a criação da pasta para alocar os nosso arquivos.

![image](https://github.com/user-attachments/assets/bba89692-90c4-4d9b-bb83-ccd61e95be11)

### Explorando os dados no Jupyter Notebook

Após montarmos o ambiente e construirmos as pastas no diretório informado, realizamos a exploração dos dados com o Jupyter Notebook e, assim, fizemos toda a análise dos dados que estão sendo coletados nos arquivos .JSON e .CSV. Verificamos a quantidade de linhas em cada arquivo, os headers (cabeçalhos) dos arquivos e imprimimos os dados contidos neles.

Como o tipo do arquivo .CSV é uma lista, foi necessário padronizar os arquivos .JSON nesse mesmo formato para que conseguíssemos unir esses dados. Para isso, realizamos todo o tratamento dos dados .JSON, incluindo a padronização da nomenclatura das colunas, de modo a unificar esses dados. Na variável KeyMapping, foi possível criar um mapeamento das chaves listadas no arquivo .JSON para que ficassem equivalentes às do arquivo .CSV.

É importante destacar que, nos dados do arquivo .JSON, não temos a chave 'Data da venda', presente no arquivo .CSV. Contudo, essa chave será incluída no arquivo consolidado, substituindo os valores em branco pela palavra "Indisponível". Isso indicará que a coluna receberá os dados futuramente, a serem fornecidos pelo departamento responsável.

![image](https://github.com/user-attachments/assets/6618ea7d-0f35-4e5b-a62b-7adeb0182b3e)

## Montando o Script

### Fusões dos dados

Explorando os dados e entendendo como eles se comportam no nosso Notebook, agora está na hora de criarmos o nosso Script para os outros tratamentos que iremos realizar futuramente. Nesta primeira etapa já estamos fazendo a extração dos dados de ambos os arquivos, renomeando as nossas colunas e unindo estes dados. Importamos a nossso "processamento_dados" e atribuíndo a classe "dados" em nosso arquivo principal para que possamos classificarmos por metódos e atributos.

![image](https://github.com/user-attachments/assets/9cac1ac3-bc2e-4cc1-82f8-52e32c1a24b0)


### Processamento dos dados

Nesta parte, estaremos classificando todo o tratamento dos dados dos dois arquivos pelo processo de atributos nesse método privado explícito em nosso código. Dentro dessa classe "dados" temos várias funções fazendo esse processamento. Uma delas é o tratamento das colunas com o List Comprehension que é muito utilizado para diminuir o tamanho do código que poderia ser utilizado, para ser mais eficiente que um for, por exemplo.

Após criarmos toda essa leitura e tratamento dos dados, iremos unir lá no final do código e salvar estes dados lá na última função criada dentro dessa classe. Isso está demonstrado na imagem 2 desse projeto. Assim, finalizando todo o tratamento dos dados e salvando em uma pasta chamada "data_processed". Esse arquivo ficará no tipo .CSV mesmo, como se trata de uma lista.

### Imagem 1:

![image](https://github.com/user-attachments/assets/ca1a339b-9f1a-4cdd-8071-ee2a318a6234)

### Imagem 2:

![image](https://github.com/user-attachments/assets/69faf4b2-92b0-43b8-b91a-c179e59f0230)

## Dados tratados

Sei que por aqui ficará meio complicado de visualizar o resultado final dess projeto, porém não poderia deixar de concluir ele demonstrando como fico esses dados dentro do nosso arquivo. Nesta primeira imagem, estará os dados .JSON que não contém os dados da chave "Data da Venda". Assim, ela ficou substituída conforme na imagem 1.

Em seguida na imagem 2, temos os dados .CSV que ficaram no final dessa junção dos dados. Nela teremos todos os dados completos, assim como a data da venda que não tinhamos no .JSON.

### Imagem 1:

![image](https://github.com/user-attachments/assets/3a24cfb1-058e-4b1e-acfb-986edd578e72)

### Imagem 2:

![image](https://github.com/user-attachments/assets/c0ca5016-b333-40de-b518-ad515b9680b4)

## Conclusão

Fiquei muito contente em aprimorar minhas habilidades com o tratamento de dados com Python. Esse projeto foi uma grande projeção de que ainda não acabou e que os estudos deverão continuar para aprimorar o raciocínio e melhorar o desempenho do código a partir das dificuldades apresentadas em nosso dia-a-dias.

Obrigado pela visita! 😉
