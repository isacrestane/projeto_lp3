#arquivo- conjunto de bytes
#transformar um arquivo csv em um dicionário
#1- ler arquivo (read)
#open--> carrega os dados do arquivoem memoria
arquivo = open("dados.txt")

#read-->lê todo o conteúdo do arquivo que esta em memoria
#chamar o read várias vezes não vai funcionar
conteudo= arquivo.read()

print(conteudo)
print(conteudo.lower())

arquivo.close()

#bloco with--> abre algum tipo de estrutura e fecha automaticamente quando o codigo sai do escopo do bloco

#if True:
#    print("1")
#    print("2")
#    print("3")
    
print ("4")

with open("dados.txt") as arquivo2:
    print(arquivo2.read())
    
#readlines retornam uma lista com as linhas    
with open("dados.txt") as arquivo3:
    linhas =arquivo3.readlines()
    print(linhas)
     

#usar direto no for (for in)
#r = read

with open("dados.txt", "r") as arquivo4:
    linhas = []
    for linha in arquivo4 :
        linhas.append(linha.strip())
    print(linhas)

#abrir no modo escrita
# w --> lê

#with open("dados.txt", "w") as arquivo5:
    #arquivo5.write("JACA")
#    pass

#abrirnomodo escrita
#a- append - escreve no final do arquivo


with open("dados.txt", "a") as arquivo6:
    arquivo6.write("\nJACA")
    


#csv--> valores separados por virgula

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos :
            dados_produto = linha.strip().split(",")
            produto = {
                "nome": dados_produto[0],
                "descricao": dados_produto[1],
                "preco": float(dados_produto[2]),
                "imagem": dados_produto[3]
            }        
            produtos.append(produto)
            
        return(produtos)
    
print(obter_produtos())


def salvar_produto(nome, descricao, preco, imagem):
    #1. abrir o arquivo em modo append "a"
    with open("produtos.csv", "a") as arquivo_produtos:
        #2. montar a string com os dados separados por vírgula
        texto_produto = f"\n{nome},{descricao},{preco},{imagem}"
        #3. escrever a string no arquivo
        arquivo_produtos.write(texto_produto)
        
salvar_produto("Celular", "Tira foto", 5.000, "celular.jpg")
salvar_produto("Fone", "Transmite musica", 500.0, "fone.jpg")

    
    
