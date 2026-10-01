#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
def tipo_investimento(opcao, valor):
    if opcao == 1:
        rendimento = (0.03 * valor)
        novo_valor = rendimento + valor
    elif opcao == 2:
        rendimento = 0.05 * valor
        novo_valor = rendimento + valor
    print(f'Atualização de valores conforme a opção {opcao}: \nRendimento: R${rendimento} \nValor corrigido: R${novo_valor}')


def main():
    tipo = int(input('--- Tipo de Investimento ---\n' \
    'Digite [1] para Poupança\n' \
    'Digite [2] para Renda Fixa\n' \
    ''))
    if tipo != 1 and tipo != 2:
            print('Opção desconsiderada')
    else:
        valor_invest = float(input('Informe o valor do investimento: R$'))
    tipo_investimento(tipo, valor_invest)

if (__name__, '__main__'):
    main()
