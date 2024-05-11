def test_success():
    cliente = Cliente()
    cadastro_Cliente = CadastroCliente()
    resposta = cadastro_Cliente.cadastrar_cliente(cliente)
    assert "Cadastro com sucesso" == resposta
