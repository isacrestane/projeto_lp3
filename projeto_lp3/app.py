#importa a classe Flask do modulo flask
from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        { "nome": "Suco de Laranja", "descricao": "Mata a sede" },
        { "nome": "Bandeja de Morangos", "descricao": "Muito bom" },
        { "nome": "Vitamina de Banana", "descricao": "Deixa forte" }
    ]

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
    
    return render_template("produtos.html", produtos=lista_produtos)


#criar uma pag que faz uma rota gerar-cpf (devover cpf aleatorio)


@app.route("/cpf")
def cpf():
    cpf = CPF()
    cpfretorno = cpf.generate(True)
    return render_template("cpf.html", cpf = cpfretorno)

    return render_template("cadastro_produto.html")
#/servicos (deve devolver um titulo com "Nossos Serviços")
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"



@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    cnpjretorno = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = cnpjretorno)


@app.route("/termos")
def termos():
    return render_template("termos.html")
app.run()

@app.route("/politica")
def politica():
    return render_template("politica.html")
app.run()

@app.route("/comousar")
def comousar():
    return render_template("comousar.html")
app.run()


@app.route("/produtos/cadastro", methods=['GET'])
def cadastro_produto():
    return render_template("cadastro_produto.html")


@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome,"descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos)

