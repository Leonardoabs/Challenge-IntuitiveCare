# Desafio Técnico Intuitive Care

Este repositório contém o código desenvolvido para o desafio técnico da Intuitive Care. O projeto foi estruturado da seguinte forma:

## 1. Teste de Web Scraping

* **Status:** Concluído.
* **Linguagem:** Python
* **Descrição:** O script em `webscrapping.py` acessa o site da ANS (`https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos`), faz o download dos Anexos I e II em formato PDF e os compacta em um único arquivo ZIP.

* **Como executar:**
    1.  Certifique-se de ter as bibliotecas `requests`, `BeautifulSoup4` e `zipfile` instaladas (`pip install requests beautifulsoup4`).
    2.  Execute o script `python webscrapping.py` a partir da raiz do projeto.
    3.  Os arquivos PDF e o arquivo ZIP compactado serão salvos no mesmo diretório.

## 2. Teste de Transformação de Dados

* **Status:** Concluído.
* **Linguagem:** Python
* **Descrição:** O script  extrai os dados da tabela do Anexo I (baixado no Teste 1), salva-os em um arquivo CSV, compacta o CSV em um arquivo ZIP chamado 


* **Como executar:** A execução está integrada com o Teste de Web Scraping (ou pode ser executado separadamente, dependendo da implementação). O arquivo CSV e o ZIP serão salvos no mesmo diretório.

## 3. Teste de Banco de Dados

* **Status:** Incompleto.
* **Linguagem:** SQL (MySQL)
* **Descrição:** Foram criados os scripts SQL (`sql/databse.sql` e `sql/tabelas.sql`) para criar o banco de dados `ans_dados` e as tabelas `demonstracoes_contabeis` e `operadoras_ativas`. No entanto, houve dificuldades na importação dos dados dos arquivos CSV baixados do site da ANS devido a erros não resolvidos. As queries analíticas para responder às perguntas sobre as maiores despesas das operadoras não foram desenvolvidas devido à falta de dados importados.

* **Arquivos SQL:** Os scripts para criação do banco e tabelas estão na pasta `sql`.
* **Observações:** A importação dos dados e as queries analíticas ficaram pendentes devido a problemas técnicos na leitura e inserção dos dados nos bancos de dados.

## 4. Teste de API

* **Status:** Funcional (com dados simulados para demonstração).
* **Linguagens:** Python (Flask), JavaScript (Vue.js)
* **Frontend:** A interface web em Vue.js (`buscador-operadoras`) permite ao usuário digitar um termo de busca e visualizar os resultados das operadoras.
    * **Como executar o Frontend:** Navegue até a pasta `buscador-operadoras` no terminal e execute `npm install` para instalar as dependências e depois `npm run serve` para iniciar o servidor de desenvolvimento do Vue.js

* **Backend:** O servidor em Python (Flask, `server.py`) possui uma rota `/busca` que recebe um termo e retorna os registros de operadoras correspondentes.

    * **Como executar o Backend:** Certifique-se de ter o Flask e o Pandas instalados (`pip install Flask pandas flask-cors`). Navegue até a raiz do projeto (onde `server.py` está localizado) e execute `python server.py`. O servidor Flask será iniciado (geralmente em `http://127.0.0.1:5000/`).

* **Demonstração no Postman:** Uma coleção no Postman (`Intuitive Care API Demo.postman_collection.json` - **se você a exportou**) foi criada para demonstrar a funcionalidade da API de busca. Devido à dificuldade na importação dos dados reais para o banco de dados, a coleção pode conter exemplos com dados simulados para ilustrar o funcionamento esperado da API.

* **Observações:** A busca no backend atualmente utiliza o arquivo CSV diretamente (ou utilizaria o banco de dados se a importação tivesse sido bem-sucedida).

## Entrega

Este é o estado atual do desafio técnico. As partes de Web Scraping e Transformação de Dados foram concluídas. O Teste de API possui um frontend e um backend funcionais (com possível demonstração simulada no Postman). O Teste de Banco de Dados ficou incompleto devido a dificuldades na importação dos dados.

Agradeço a oportunidade e fico à disposição para quaisquer esclarecimentos.