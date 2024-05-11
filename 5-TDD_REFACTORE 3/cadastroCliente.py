class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):

        if cliente.idade < 18:
            return "Cliente menor de idade, nao cadastrado"

        self.clientes_cadastrados.append(cliente)

        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com sucesso"
        
