# Estruturas condicionais e de repetição.

# - Identação e blocos de comando - define onde um bloco de comando começa e termina
# Em python, não tem {} ou ;, mas teve respeitar os espaços dos blocos
# Para começar o bloco é só colocar ":"

# - Estruturas condicionias, permite odesvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

# IF - irá testar a expressão lógica, e em caso de retorno verdadeiro, o bloco do if é executado.

# IF / ELSE - dois desvios testados, se a lógica testado no if não foi verdadeira, o bloco do else é executado.
saldo = 2000
saque = float(input ("Informe o valor do saque"))

if saldo >= saque:
    print ("Realizando saque")
else:
    print("Saldo insuficiente!")


# ELIF - 2 ou + desvios testados, ele é testados e caso retorne verdadeiro, o bloco dele é executado.
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque:"))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    SystemExit("Opção inválida")


# IF ANINHADO - estrtuturas de if/elif/else dentro do bloco de if/elif/else
saldo = 2000
saque = 2500
conta_normal = True
conta_universitario = False
cheque_especial = 450

if conta_normal:
    if saldo>= saque:
        print("Saque realizado com sucesso!!!")
    elif saque <= (saldo+cheque_especial):
        print("Saldo insuficiente")
    else:
        print ("Não foi possível realizar saque, sem saldo")
elif conta_universitario:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")


# IF TERNARIO - condição em uma única linha dividida em 3 partes: 1 e o retorno caso seja verdadeiro, 2 expressão lógica e 3 caso o retorno não seja atendida.
status = "sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque!")

