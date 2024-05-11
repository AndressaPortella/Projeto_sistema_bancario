#Projeto sistema bancário
#Autora: Andressa Silva Gomes
#Data: 10/05/2024
saldo = 0
valor_deposito = 0
valor_saque = 0
LIMITE_SAQUE_DIARIO = 2
LIMITE_VALOR_SAQUE = 500.00
quantidade_saque = 0
quantidade_deposito = 0
total_deposito = 0
total_saque = 0
deposito = ""
saque = ""
menu = ("""
    ------- BANCO BATATA FRITA🍟-------

     Bem vindo ao banco Batata Frita!
            Escolha uma opção:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    -----------------------------------

""")

print (menu)
opcao = str

while opcao != 0:
    opcao = (input("Digite uma opção: "))
    if opcao == "1":
        valor_deposito = float(input("Digite um valor a ser depositado: "))
        print("-----------------------------------")
        if valor_deposito > 0:
            print(f"O valor depositado foi de R$ {valor_deposito:.2f}")
            saldo = saldo + valor_deposito
            total_deposito = total_deposito + valor_deposito
            quantidade_deposito += 1
            deposito += f"| - Valor Depositado = R${valor_deposito:.2f}\n"
            print(f"Seu saldo atual é de R${saldo:.2f}")
            print("")
            print (menu)
        elif valor_deposito == 0 or valor_deposito < 0:
            print("Valor digitado inválido!")
            print("")
            print(menu)

    elif opcao == "2":
        print("-----------------------------------------")
        print(f"O saldo da sua conta é: R${saldo:.2f}")
        print("")
        if saldo == 0:
            print ("Não é possível sacar, saldo insuficiente!")
            print ("")
            print (menu)
        elif saldo > 0:
            valor_saque = float(input("Digite um valor para sacar: "))
            print("")

            if valor_saque > 0:
                if (quantidade_saque <= LIMITE_SAQUE_DIARIO):
                    if (valor_saque <= LIMITE_VALOR_SAQUE) and (saldo >= valor_saque):
                        saldo = saldo - valor_saque
                        total_saque = total_saque + valor_saque
                        quantidade_saque += 1
                        saque += f"| - Valor Sacado = R${valor_saque:.2f}\n"
                        print("")
                        print("Saque realizado com sucesso!")
                        print (f"Seu saldo atual é de R${saldo:.2f}")
                        print("")
                        print(menu)
                    elif (valor_saque > LIMITE_VALOR_SAQUE):
                        print("")
                        print("O valor de saque não pode ser superior a R$500,00!")
                        print(menu)
                    else:
                        ("")
                        print("Valor insuficiente! Faça um depósito em sua conta para sacar.")
                        print("")
                        print(menu)
                elif (quantidade_saque > LIMITE_SAQUE_DIARIO):
                    print("")
                    print("Limite de saque diário atingido! Tente novamente em 24h.")
                    print("")
                    print(menu)
            elif valor_saque == 0 or valor_saque < 0:
                print("Valor digitado inválido!")
                print("")
                print(menu)

    elif opcao == "3":
        extrato = (f"""
--------- EXTRATO BANCÁRIO ---------:
|
{deposito}
{saque}
|
| - Quantidade de saques = {quantidade_saque}  
| - Valor total depositado = R${total_deposito:.2f}
| - Quantidade de depósitos = {quantidade_deposito}
| - Valor total sacado = R${total_saque:.2f}
|
|  Saldo atual da conta = R${saldo:.2f}
|
=====================================
            
            """)
        if (quantidade_deposito > 0) or (quantidade_saque > 0):
            print (extrato)
            print (menu)
        elif (quantidade_deposito == 0) and (quantidade_saque == 0):
            print("")
            print ("Não foram realizadas movimentações.")
            print ("-----------------------------------")
            print (menu)

    elif opcao == "0":
        print("Operação finalizada!")
        print("Agradecemos por ser nosso cliente! Volte sempre!👋🏼")
        break

    else:
        print("Opção inválida!")
        print(menu)
        
        
