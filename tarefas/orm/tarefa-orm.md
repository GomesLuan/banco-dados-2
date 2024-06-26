# Resumo ODBC

O ODBC (Open Database Connectivity) é uma API padrão que permite que aplicativos se conectem a diferentes bancos de dados relacionais de forma consistente. Em Python, pode ser utilizado o módulo pyodbc para interagir com bancos de dados via ODBC. Para utilizar o ODBC em Python, primeiro deve-se estabelecer uma conexão com o banco de dados usando pyodbc.connect(), fornecendo os detalhes de conexão. Em seguida, cria-se um cursor para executar consultas SQL e processar os resultados. Depois de concluir as operações, deve-se confirmar as alterações e fechar a conexão e o cursor.

# Resumo ORM

ORM (Object-Relational Mapping) é uma técnica que permite mapear objetos de linguagens de programação para tabelas em um banco de dados relacional, simplificando o processo de interação com o banco de dados. Em Python, uma das bibliotecas mais populares para ORM é o SQLAlchemy. Com o SQLAlchemy, são definidas classes que representam as tabelas do banco de dados e os relacionamentos entre elas. Essas classes são conhecidas como modelos ou classes de entidade. O SQLAlchemy gera consultas SQL automaticamente com base nas operações realizadas nos objetos dessas classes. Isso significa que, em vez de escrever consultas SQL manualmente, pode-se manipular objetos Python e o SQLAlchemy se encarrega de traduzir essas operações em instruções SQL apropriadas.

# Links para scripts

- [ORM](orm.py)
- [ODBC](odbc.py)