from time import sleep
from os import system

menu = """
        Sistema Bancário
    ************************
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair da Conta
    ************************
    
    :
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    try:
        opcao = int(input(menu))

        if opcao == 1:
            system("cls") or None
            print("Deposito:\n*********\n")

            depositar = float(input("Valor a depositar R$"))

            while True:
                resposta_deposito = int(
                    input(
                        f"Confirmar o deposito de valor R${str(depositar).replace(".", ",")}\n[1] Sim [2] Não\n:"
                    )
                )

                if resposta_deposito == 1:
                    float(depositar)
                    saldo += depositar
                    numero_saques += 1
                    extrato += f"Depositado R${str(depositar).replace(".", ",")}\n"
                    print("Depósito concluído com sucesso...")
                    sleep(2)
                    system("cls") or None
                    break

                elif resposta_deposito == 2:
                    print("Operação cancelada.")
                    print("Retornando ao menu principal...")
                    sleep(2)
                    system("cls") or None
                    break

                else:
                    print("Opção inválida. Por favor tente novamente...")

        elif opcao == 2:
            system("cls") or None
            print("Saque:\n******\n")
            sacar = float(input("Valor a sacar R$"))

            while True:
                resposta_saque = int(
                    input(f"\nConfirmar o saque de R${str(sacar).replace(".", ",")}?\n[1] Sim [2] Não\n:")
                )

                if resposta_saque == 1:
                    if numero_saques <= LIMITE_SAQUES:
                        if saldo >= sacar and sacar <= 500:
                            float(sacar)
                            saldo -= sacar
                            numero_saques += 1
                            extrato += f"Saque R${str(sacar).replace(".", ",")}\n"
                            print("Saque concluído com sucesso...")
                            sleep(2)
                            system("cls") or None
                            break

                        elif sacar > 500 and saldo > 500:
                            print(
                                'O limite por tentativa de saque é de R$500,00... Por favor tente novamente!"'
                            )
                            sleep(2)
                            system("cls") or None
                            break

                        else:
                            print("Você não possui saldo suficiente em conta...")
                            sleep(2)
                            system("cls") or None
                            break
                    else:
                        print(
                            "Você atingiu o limite de saque diário. Por favor tente novamente no próximo dia..."
                        )
                        sleep(2)
                        system("cls") or None
                        break
                elif resposta_saque == 2:
                    print("Operação cancelada.")
                    break

                else:
                    print("Opção inválida. Por favor tente novamente...")
                    sleep(2)
                    system("cls") or None

            print("Retornando ao menu principal...")
            sleep(1)
            system("cls") or None

        elif opcao == 3:
            system("cls") or None
            print("Extrato:\n********\n")

            if extrato == "":
                print("Não foram realizadas movimentações")
            else:
                print(extrato, f"\nSaldo: R${str(saldo).replace(".", ",")}")
            sleep(5)
            system("cls") or None

        elif opcao == 0:
            system("cls") or None
            print("Encerrando o sistema...")
            break

        else:
            print("Operação inválida. Por favor selecione novamente a opção desejada.")

    except ValueError:
        print(
            "Valor inválido, por favor digite apenas o número da opção que deseja acessar..."
        )

sleep(1)
print("Obrigado por utilizar nossos serviços. Volte sempre!")
