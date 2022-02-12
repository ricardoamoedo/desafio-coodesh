# API REST sobre MySQL com FastAPI

Este projeto oferece uma solução do desafio proposto pela Coodesh (challenge by coodesh) como teste de habilidades para desenvolvedor Back-end, e nele esta implementada uma REST API com base em uma já existente, (utilizando Web Scraping)  para posterior conexão de outras aplicações.



## Linguagens, Frameworks e Bibliotecas 

* Python
* FastAPI
* uvicorn
* mysql-connector-python
* python-sqlalchemy
* requests


## Instruções

1. O banco de dados MySQL encontra-se no servidor Heroku, sendo que os dados de acesso a conexão encontram-se no script "db.py", dentro da pasta config.

	Fonte: [https://elements.heroku.com/addons/jawsdb](https://elements.heroku.com/addons/jawsdb)


2. Criando e ativando o ambiente virtual

  
	- python3 -m venv env

	- source venv/bin/activate (no linux)

3. baixando o projeto do Github

  
	- git init

	- git clone https://github.com/ricardoamoedo/desafio-coodesh.git

  
4. Instalando frameworks e bibliotecas:

  
	- pip install -r requirements.txt
  
5. Executando o Uvicorn

	- execute o no terminal uvcorn pelo comando “uvicorn main:app --reload”


6. Utilizando o CRON para a automatização de processos no Linux

	- mova a pasta “cron” e seu conteúdo para a sua pasta de usuário.

 
	- no terminal, abra o crontab com o seguinte comando: “crontab -e” e adicione na última linha a seguinte expressão “0 9 * * * python /_home_/{usuário}/cron/cronUpdate.py”. Para adicionar a expressão é necessário primeiramente teclar “i” de inserir, e após adicionada a expressão pressione a tecla shift + a tecla : e digite wq seguido de enter.

    **OBS: Não esqueça de mudar o nome {usuário} para o seu nome de usuário do computador.**

## Vídeo de apresentação do projeto

	- link: 
