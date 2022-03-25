#Exercício 48 – Soma ímpares múltiplos de três

#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#soma = []
soma = 0
for i in range(3, 500, 3):
    soma += i
    #soma.append(i)

#soma = sum(soma)
print(soma)