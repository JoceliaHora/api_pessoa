import json


def testeBanco():
    return "teste banco OK"


def listarPessoas():     
    with open('src/sample.json', 'r') as openfile:  #abrindo arquivo
        json_object = json.load(openfile)  # convertendo o conteudo do arquivo em obj json
        return json_object                      # retornando json

def salvaNoBanco(pessoa):

    with open("src/sample.json", "r") as outfile:  #abre o arquivo
        dic = json.load(outfile)               #converte o conteudo do arquivo pra um obj json
        dic.append(pessoa)                  #adicionar elemento dentro de uma lista
        json_object = json.dumps(dic, indent=4)    # convertendo de json pra string
        with open("src/sample.json", "w") as outfile:  #abrindo arquivo 
            outfile.write(json_object)             #gravando as informações no arquivo


    return "pessoa salva com sucesso "