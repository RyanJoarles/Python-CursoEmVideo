#Exercício 49 – Tabuada v.2.0

#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(0, 11, 1):
    print("{} x {} =".format(num, i), num*i)