#Exercício 51 – Progressão Aritmética

#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

for i in range(1, 11, 1):
    num += razao
    print(num, end=' ')