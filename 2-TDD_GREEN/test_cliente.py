from cliente import Cliente
from cadastroCliente import CadastroCliente

def test_success():
    cliente = Cliente("Gerson", 26, "gerson@test.com")
    cadastro_Cliente = CadastroCliente()
    resposta = cadastro_Cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta
