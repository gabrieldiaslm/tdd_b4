from cliente import Cliente
from cadastroCliente import CadastroCliente

def test_success():
    cliente = Cliente("Gerson", 26, "gerson@test.com")
    cadastro_Cliente = CadastroCliente()
    resposta = cadastro_Cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta

def test_idade():
    cliente = Cliente("Pedro", 16, "pedro@test.com")
    cadastro_Cliente = CadastroCliente()
    resposta = cadastro_Cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idade, nao cadastrado" == resposta
