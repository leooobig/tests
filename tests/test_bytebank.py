from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #Given-Context
        entrada = '13/03/2000'
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        #When-Action
        resultado = funcionario_teste.idade()

        
        assert resultado == esperado #Then-outcome