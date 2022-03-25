#Exercício 50 – Soma dos pares

#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for num in range(0, 6, 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num

print(soma)
