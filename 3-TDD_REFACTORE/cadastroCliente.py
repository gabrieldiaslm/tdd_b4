class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):
        self.clientes_cadastrados.append(cliente)
        return "Cadastrado com sucesso"

        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com Sucesso"