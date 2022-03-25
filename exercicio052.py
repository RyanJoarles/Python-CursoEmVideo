#Exercício 52 – Números primos

#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


while True:
    num =  int(input('Digite um número: '))

    p = True

    for i in range(2, num + 1, 1):
        resto = num % i

        if resto == 0:
            if  i != num:
                print(num, 'não é primo!')
                p = False
                break

    if p == True:
        print(num, 'é primo!')

            
        
        
