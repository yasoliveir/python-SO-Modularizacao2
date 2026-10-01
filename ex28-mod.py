#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço

def calculo_preco_novo(atual, media):
    if (atual < 30.00) and (media < 500):
        preco_novo = atual + (0.1 * atual)
    elif (atual >= 30.00 and atual  < 80.00) and (media >= 500 and media < 1000):
        preco_novo = atual + (0.15 * atual)
    elif (atual >= 80.00) and (media >= 1000):
        preco_novo = atual - (0.05 * atual)
    else: 
        preco_novo = atual
    print(f'O valor do produto atualizado é de R${preco_novo}')
    
def main():
    preco_atual = float(input('Preço atual: '))
    media_mensal = float(input('Média mensal: '))
    calculo_preco_novo(preco_atual, media_mensal)

if (__name__, '__main__'):
    main()