import json


def testeBanco():
    return "teste banco OK"


def listarPessoas():     
    with open('src/sample.json', 'r') as openfile:  #abrindo arquivo
        json_object = json.load(openfile)  # convertendo o conteudo do arquivo em obj json
        return json_object                      # retornando json
