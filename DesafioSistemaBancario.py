# Desafio - sistema bancário

saldo_atual = 0
limite_saque = 500
historico_transacoes = ""
contagem_saques = 0
max_saques = 3

menu_principal = """
[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair
Digite aqui:"""

while True:
    opcao = input(menu_principal)

    if opcao == "a":
        valor_deposito = float(input("Digite o valor a ser depositado: "))

        if valor_deposito > 0:
            saldo_atual += valor_deposito
            historico_transacoes += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação inválida! O valor deve ser positivo.")

    elif opcao == "b":
        valor_saque = float(input("Digite o valor a ser sacado: "))

        saldo_insuficiente = valor_saque > saldo_atual
        limite_excedido = valor_saque > limite_saque
        saques_excedidos = contagem_saques >= max_saques

        if saldo_insuficiente:
            print("Erro! Saldo insuficiente.")
        elif limite_excedido:
            print("Erro! O valor do saque ultrapassa o limite permitido.")
        elif saques_excedidos:
            print("Erro! Limite de saques excedido.")
        elif valor_saque > 0:
            saldo_atual -= valor_saque
            historico_transacoes += f"Saque: R$ {valor_saque:.2f}\n"
            contagem_saques += 1
        else:
            print("Operação inválida! O valor deve ser positivo.")

    elif opcao == "c":
        print("\n== EXTRATO ==")
        print("Nenhuma movimentação realizada." if not historico_transacoes else historico_transacoes)
        print(f"\nSaldo: R$ {saldo_atual:.2f}")
       
    elif opcao == "d":
        print("Saindo do sistema...")
        break

    else:
        print("Insira uma opção válida.")
