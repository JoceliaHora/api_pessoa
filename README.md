

### instalando dependências

  

#### Flask - primeiros passos

  

    https://pythonbasics.org/flask-tutorial-hello-world/

  

#### Flask - trabalhando com parametros

  

    https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-pt


### Testando meus endpoints

#### Endpoint de teste  (GET)

    http://127.0.0.1:81/    

#### Edpoint Cadastrar (POST)

    http://127.0.0.1:81/ 
Body

    {
	"cpf": "123.456.789.89",
	"nome": "jocelia",
	"endereco": "rua das ortencias"
	}
#### Endpoint de buscar pessoa (GET)

    http://127.0.0.1:81/buscar?cpf=123

#### Endpoint de listar pessoas (GET)

    http://127.0.0.1:81/listar

#### Endpoint de delepar pessoas (DELETE)

    http://127.0.0.1:81/?cpf=123
