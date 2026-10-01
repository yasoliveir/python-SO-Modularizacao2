#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def calculo_vm(voltas, extensao_m, tempo_minutos):
    distancia_total = (extensao_m * voltas) / 1000
    tempo_horas = tempo_minutos / 60
    vm = distancia_total / tempo_horas
    print(f'Distância total: {distancia_total:.0f} km ')
    print(f'Tempo total: {tempo_horas:.2f} h ')
    print(f'A velocidade média é de {vm:.2f} km/h')

def main():
    num_voltas = int(input('Número de voltas: '))
    extensao = float(input('Extensão do circuito (em metros): '))
    tempo = int(input('Duração (em minutos): '))
    calculo_vm(num_voltas, extensao, tempo)
    

if (__name__, '__main__'):
    main()