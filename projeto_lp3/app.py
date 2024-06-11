#importa a classe Flask do modulo flask
from flask import Flask

#Aluno a1 = new aluno();
#a1= Aluno()

#instancia um objeto flask que representa a aplicação
app = Flask ("Minha Aplicação")

#rota + função 
#rota: definição de um padrao url
#função: função python com retorno (string,template, outro)

#pagina home -/
@app.route("/")
def home():
    return "<h1>Home page</h1>"

#pagina de contato - /contato

@app.route("/contato")
def contato():
    return "<h1>Contatos</h1>"


@app.route("/produto")
def produtos():
    return "<h1>Produtos</h1>"

