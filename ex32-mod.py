#Receba um número inteiro. Calcule e mostre o seu fatorial.
def fatorial(valor):
    aux = valor
    cont = valor
    for i in range(valor-1, 0, -1):
        aux = i * aux
        print(f'{valor}x{i} = {aux}')
        valor = aux
    print('-'*30)
    print('O resultado de ',cont,'! é:',aux)
def main():
    n = int(input('Numero: '))
    fatorial(n)

if (__name__, '__main__'):
    main()
