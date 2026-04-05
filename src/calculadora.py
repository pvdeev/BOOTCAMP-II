def validar_valor(valor):
    if valor >= 0:
        return True
    else:
        return False


def calcular_saldo(renda,despezas):
    return renda - despezas

def verificar_meta(saldo,meta):
    if saldo >= meta:
        return 'parabens! voce alcancou sua meta.'
    else:
        diferenca = meta - saldo
        return f'ainda falta {diferenca} para alcancar a meta.'
    

renda_usuario = (float(input('digite sua renda: ')))
despesa_usuario = (float(input('digite suas despesas: ')))
meta_usuario = (float(input('digite sua meta:')))

if validar_valor(renda_usuario) and validar_valor(despesa_usuario):
    meu_saldo = calcular_saldo(renda_usuario, despesa_usuario)
    resultado = verificar_meta(meu_saldo, meta_usuario)
    print(f"Saldo atual: {meu_saldo}")
    print(resultado)
else:
    print("Erro: Os valores inseridos não podem ser negativos.")