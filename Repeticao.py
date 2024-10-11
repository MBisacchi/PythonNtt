# Estrtuturas de repetição - são usadas para repitir um trecho de código, um quatidade de x.

# FOR - Percorre um objeto iterável, usado quando sabe quantas vezes deve se repetir
print ("-FOR-")
texto = input("Informe um texto:")
VOGAIS = "AEIOU"
# o 'for' percorre letra a letra até terminar o que precisa e o 'upper' serve para deixar todas as letras maiúsculas.
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print ("Executa o final do laço")


# RANGE - é uma função built-in do python, ela produz uma sequência de números int a partir de um ínicio (inclusivo), fim (exclusivo)
# recebe ainda 3 argumentos: stop (obrigatório), start (opcional) e step opcional.
# sintax: range (stop) -> range object
#         range (start, stop [, step]) -> rand object
print ("-RANGE-")
list(range(4))

# Range com for (1- ir até o número definido e 2- exibindo a tabuada do 5)
for numero in range (11):
    print(numero, end="")

for numero in range (0,51,5):
    print (numero, end="")


# WHILE - Repete o bloco de código e é usado quando não se sabe quantas x deve repetir, não tem saida até colocar uma opção válida
print ("\n-WHILE-")
opcao = -1

while opcao != 0:
    opcao = int (int (input("[1] Sacar \n [2] Extrato \n [0] Sair \n:")))
    if opcao == 1:
        print ("Sacando ...")
    elif opcao == 2:
        print ("Exibindo o extrato ...")


# WHILE/ELSE - Repete um código e tem uma saída
print ("-WHILE/ELSE-")
while opcao != 0:
    opcao = int (int (input("[1] Sacar \n [2] Extrato \n [0] Sair \n:")))
    if opcao == 1:
        print ("Sacando ...")
    elif opcao == 2:
        print ("Exibindo o extrato ...")
else:
    print ("Obrigada!!")


# WHILE COM BREAK - corta a execução
print ("-WHILE COM BREAK-")
while True:
    numeroBreak = int(input("Informe um número:"))
    if numeroBreak == 10:
        break
    
    print(numeroBreak)


# WHILE COM CONTINUE - pula a execução
print ("-WHILE COM CONTINUE-")
while True:
    numero = int(input("Informe um número:"))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    print(numero)