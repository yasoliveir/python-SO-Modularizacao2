#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
def calculo_soma(valor):
    soma = 1
    fatorial = 1 
    for i in range (1, valor+1):
        fatorial = fatorial * i 
        soma += 1 / fatorial 
    print(f"O resultado da série para N = {valor} é {soma:.2f}")
def main():
    n = int(input('Número: '))
    calculo_soma(n)

if (__name__, '__main__'):
    main()
