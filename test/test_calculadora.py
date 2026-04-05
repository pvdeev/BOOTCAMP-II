import unittest
import sys
import os

# Esse bloco garante que o Python encontre a pasta 'src' para importar seu código
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculadora import calcular_saldo, validar_valor, verificar_meta

class TestCalculadoraEconomia(unittest.TestCase):

    # 1. TESTE: CAMINHO FELIZ (Cenário Correto)
    def test_calcular_saldo_positivo(self):
        # Se eu ganho 3000 e gasto 2000, o saldo DEVE ser 1000
        resultado = calcular_saldo(3000, 2000)
        self.assertEqual(resultado, 1000)

    # 2. TESTE: ENTRADA INVÁLIDA (Valor Negativo)
    def test_validar_valor_negativo(self):
        # A função deve retornar False se o valor for negativo
        self.assertFalse(validar_valor(-50))

    # 3. TESTE: CASO LIMITE (Saldo exatamente igual à meta)
    def test_meta_exata(self):
        # Se o saldo é 500 e a meta é 500, a mensagem deve ser de sucesso
        mensagem = verificar_meta(500, 500)
        self.assertIn('Parabéns', mensagem)

if __name__ == '__main__':
    unittest.main()