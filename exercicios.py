import os
import time 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
tempo = 3
contador = True

while contador == True:
    limpar_tela()
    print("EXERCICIOS PYTHON-------")
    print("ESTRUTURA SEQUENCIAL - 1")
    print("ESTRUTURA DECISÃO - 2")
    print("para fechar digite - 0")
    opcao = int(input("digite a lista de exercicios que quer visualizar - "))
    match opcao:
        case 0: 
            contador = False
        case 1: 
            opcaoSeq = int(input("- EXERCICIOS (1 ao 10)"))
            match opcaoSeq:
                case 0: 
                    contador = False 
                case 1: 
                    print("Escolha do Numero--------------") 
                    x = int(input("digite um numero "))
                    print(f"o numero é {x}")
                case 2: 
                    print("Dois Números--------------")
                    x = int(input("Digite um numero: "))
                    y = int(input("Digite um segunto numero:"))
                    soma = x + y 
                    print(f"A soma dos numeros é: {soma}")

                case 3: 
                    print("Calculo de Media--------------")
                    n1 = int(input("digite nota 1"))
                    n2 = int(input("nota 2: "))
                    n3 = int(input("nota 3: "))
                    n4 = int(input("nota 4: "))
                    media = (n1+n2+n3+n4)/4
                    print(f"a media das notas é: {media}")
                case 4: 
                    print("COnversor de Metros----------")
                    metros = int(input("Digite um numero em metros: "))
                    cent = metros*100
                    print(f"Esse numero em cm é: {cent}")

                case 5: 
                    print("Raio de Circulo--------------")
                    raio = int(input("Digite o Raio de um circulo: "))
                    calcRaio = 3.14 * (raio * raio)
                    print(f"A area do ciculo é: {calcRaio}")
                case 6:
                    print("Dobro Área de Quadrado-------------")
                    lado = int(input("Digite o Tamanho do Lado de um quadrado: "))
                    calcArea = (lado * lado) * 2 
                    print(f"O drobro da area desse quadrado é {calcArea}")
                case 7: 
                    print("Programa de Calculo Salarial-------")
                    horasTrab = int(input("informe as suas horas trabalhadas: " ))
                    salHora = int(input("informe o seu salario por hora: "))
                    diasMes = 30
                    calcSalario = (salHora * horasTrab) * diasMes
                    print(f"seu salario é: {calcSalario}")
                case 8: 
                    print("CALCULO DE FAHRENHEIT-------------")
                    f = int(input("informe a temparatura em F: "))
                    calcCelcius = 5 * ((f-32) /9)
                    print(f"em celcius é{calcCelcius}")

                case 9: 
                    print("CALCULO DE CELCIUS--------------")
                    c = int(input("informe a temparatura em F: "))
                    calcF = (c * 9/5) + 32
                    print(f"em celcius é{calcF}")
                case 10: 
                    print("CALCULO DE 2 NUMEROS INTEIROS e UM REAL---")
                    n1 = int(input("numero 1: "))
                    n2 = int(input("numero 2: "))
                    n3 = float(input("um numero Real: "))
                    produto = (n1 * 2) * (n2/2)
                    print(f"O produto do dobro do primeiro com metade do segundo {produto}")
                    soma = (n1 * 3) + n3
                    print(f"A soma do triplo do primeiro com o terceiro {soma}")
                    cubo = n3 ** 3
                    print(f"O terceiro elevado ao cubo{cubo}")
                case _:
                    print("oção invalida!")
            time.sleep(tempo)
        case 2: 
            opcaoDec = int(input("EXERCICIOS 1 ao 10"))
            match opcaoDec: 
                case 1: 
                    print("MAIOR NUMERO-------------")
                    n1 = int(input("numero 1: "))
                    n2 = int(input("numero 2: "))
                    if n1 > n2: 
                        print(f"maior numero {n1}")
                    if n2 > n1: 
                        print(f"maior numero é: {n2}")
                    else: 
                        print("são numeros iguais:")
                case _:
                    print("numero invalido!")
        case _:
            print("numero invalido!!")