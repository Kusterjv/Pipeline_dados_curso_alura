# Pipeline de dados

Neste projeto foi abordado a seguinte situação: Duas empresas se unificaram e agora precisam dos dados da empresaA e empresaB unidos. Porém, esses dados não estão no formato esperado e por isso foi criado este pipeline para extrair, tratar e carregar os dados. O famoso ETL.

## Criação das pastas da pipeline em um WSL

Esse processo foi crucial para colocarmos em pauta onde serão alocados as pastas e arquivos que estaremos trabalhando. Dessa forma, foi pensando em colocar em WSL (Windows Subsystem for Linux). Que é um subsistema do Linux no Windows onde estarei manipulando estes arquivos e criando pastas para organizar todo o projeto.

Na imagem abaixo, estamos chamando o 'dir' para listarmos as pastas criadas nesse caminho. Como já temos uma pasta "Documentos" criada, onde ficará os arquivos do nosso projeto, não será necessário utilizar o comando 'mkdir' para a criação da pasta para alocar os nosso arquivos.

## Rodando o VSCode no nosso ambiente virtual

![image](https://github.com/user-attachments/assets/bba89692-90c4-4d9b-bb83-ccd61e95be11)

Após montarmos o ambiente e construir as pastas no diretório informado, realizamos a exploração dos dados com o Jupyter Notebook e assim fazemos toda a análise dos dados que estão sendo coletados nos arquivos .JSON e .CSV. Verificamos ali a quantidade de linhas em cada arquivo, cada Header (cabeçalho) dos arquivos e imprimindo os dados que contém neles.

## Explorando os dados no Jupyter Notebook

