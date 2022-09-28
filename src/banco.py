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



def deletarPessoa(cpf):
    with open('src/sample.json', 'r') as openfile:   #abre o arquivo
        dic = json.load(openfile)                  #converte pra json
        for objeto in dic:                         # for pra varrer os elementos da lista
            if objeto["cpf"] == cpf:                #if compara qual cpf quero remover
                index = dic.index(objeto)           #encontrando a posição do obj na lista
                dic.pop(index)                      #removendo o elemento no indice encontrado com pop
                json_object = json.dumps(dic, indent=4)     # convertendo pra string
                with open("src/sample.json", "w") as outfile:   #abrindo o arquivo em modo de escrita
                    outfile.write(json_object)              #gravando a lista sem o elemento deletado no meu arquivo 
                return "Pessoa removida"                    
    return "CPF nao foi encontrado!"