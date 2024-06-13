#importa a classe Flask do modulo flask
from flask import Flask
from validate_docbr import CPF, CNPJ

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


#criar uma pag que faz uma rota gerar-cpf (devover cpf aleatorio)


@app.route("/gerar-cpf")
def cpf():
    cpf = CPF()
    return cpf.generate(True)


#/servicos (deve devolver um titulo com "Nossos Serviços")
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"


#
@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    return cnpj.generate(True)

app.run()
