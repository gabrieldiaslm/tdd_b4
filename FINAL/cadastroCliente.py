idade_min = 18
email_char = "@"


class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):

        if cliente.idade < idade_min:
            return "Cliente menor de idade, nao cadastrado"

        if email_char not in cliente.email:
            return "Email invalido, nao cadastrado"

        self.clientes_cadastrados.append(cliente)

        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com sucesso"
        
