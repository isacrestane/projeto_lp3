#importa a classe Flask do modulo flask
from flask import Flask, render_template
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
    return render_template("home.html")

#pagina de contato - /contato

@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/produtos")
def produtos():
    lista_produtos = [
        { "nome": "Coca-Cola", "descricao": "Mata a sede" },
        { "nome": "Doritos", "descricao": "Suja a mao" }
    ]
    return render_template("produtos.html", produtos=lista_produtos)


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
