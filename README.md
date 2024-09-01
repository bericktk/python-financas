## Descrição
Este projeto Python tem como objetivo coletar dados históricos de cotações de ativos financeiros e armazená-los em um banco de dados MySQL.

## Funcionalidades Principais
* **Conexão com o banco de dados:** Utiliza a biblioteca `mysql.connector` para estabelecer uma conexão com um banco MySQL, configurado com as credenciais e informações de conexão específicas.
* **Coleta de dados:** Emprega a biblioteca `yfinance` para obter dados históricos de cotações de ativos financeiros, definindo um período de tempo e uma lista de ativos.
* **Inserção de dados:** Insere os dados coletados em uma tabela do banco de dados, formatando os dados para corresponder à estrutura da tabela.
* **Gerenciamento de erros:** Implementa mecanismos para lidar com possíveis erros durante a conexão com o banco de dados e a inserção dos dados.

## Pré-requisitos
* **Python 3.12:** Instalar a versão do Python compatível com as bibliotecas utilizadas.
* **Bibliotecas:** Instalar as seguintes bibliotecas utilizando o gerenciador de pacotes pip:
  ```bash
  pip install mysql-connector-python pandas yfinance
* **Banco de dados MySQL:** Ter um banco de dados MySQL configurado e uma tabela criada para armazenar os dados. A estrutura da tabela deve corresponder àquela utilizada no script.

## Uso
**Configuração:**
* **Credenciais:** Modifique as credenciais de conexão com o banco de dados no dicionário conexao.
* **Tabela:** Certifique-se de que a tabela no banco de dados possui os campos corretos para armazenar os dados coletados.

## Execução:
Execute o script Python.
Os dados serão coletados e inseridos no banco de dados de acordo com os parâmetros definidos no script. Até o momento foi criado apenas a função para inserir os dados na tabela, faltando criar as funções de visualizar, atualizar e deletar.

## Personalização
* **Ativos:** Modifique a lista ativos para incluir os ativos desejados. A lista de Ativos pode ser alterada para adicionar outros ativos conforme biblioteca Yfinance.
* **Período:** Altere as datas data_inicial e data_final para definir o período de coleta de dados. As váriaveis de data_inicial e data_final podem ser alteradas para visualização de novas datas.
* **Banco de dados:** Ajuste as informações de conexão com o banco de dados e a estrutura da tabela conforme seu banco de dados.

## Autores
* **Bruno Erick**

## Tecnologias e Bibliotecas
* **VS Code**
* **Python**
* **YFinance**
* **Pandas**
* **SQL**
* **MariaDB**
