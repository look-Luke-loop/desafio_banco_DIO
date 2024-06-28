# main.py
import contas

def criar_usuario(lista_usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in lista_usuarios:
        if usuario[2] == cpf:
            print("Usuário com este CPF já cadastrado!")
            return lista_usuarios
    
    novo_usuario = [nome, data_nascimento, cpf, endereco]
    lista_usuarios.append(novo_usuario)
    return lista_usuarios

def main():
    lista_usuarios = []
    lista_contas = []
    
    while True:
        print("\nBem-vindo ao Banco!")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Sacar")
        print("4. Depositar")
        print("5. Ver Extrato")
        print("6. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("CPF: ")
            endereco = input("Endereço (logradouro - bairro - cidade/sigla estado): ")
            lista_usuarios = criar_usuario(lista_usuarios, nome, data_nascimento, cpf, endereco)

        elif opcao == '2':
            cpf = input("Digite o CPF do usuário: ")
            lista_contas = contas.criar_conta(lista_contas, lista_usuarios, cpf)

        elif opcao == '3':
            agencia = input("Digite o número da agência: ")
            numero_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor do saque: "))
            
            conta_encontrada = None
            for c in lista_contas:
                if c[0] == agencia and c[1] == numero_conta:
                    conta_encontrada = c
                    break
            
            if conta_encontrada:
                saldo, extrato, numero_saques = conta_encontrada[3], conta_encontrada[4], len(conta_encontrada[4])
                saldo, extrato, numero_saques = contas.sacar(
                    saldo=saldo, valor=valor, extrato=extrato, limite_valor=500, 
                    numero_saques=numero_saques, limite_saques=3
                )
                conta_encontrada[3], conta_encontrada[4] = saldo, extrato
            else:
                print("Conta não encontrada!")

        elif opcao == '4':
            agencia = input("Digite o número da agência: ")
            numero_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor do depósito: "))
            
            conta_encontrada = None
            for c in lista_contas:
                if c[0] == agencia and c[1] == numero_conta:
                    conta_encontrada = c
                    break
            
            if conta_encontrada:
                saldo, extrato = conta_encontrada[3], conta_encontrada[4]
                saldo, extrato = contas.depositar(saldo, valor, extrato)
                conta_encontrada[3], conta_encontrada[4] = saldo, extrato
            else:
                print("Conta não encontrada!")

        elif opcao == '5':
            agencia = input("Digite o número da agência: ")
            numero_conta = input("Digite o número da conta: ")
            
            conta_encontrada = None
            for c in lista_contas:
                if c[0] == agencia and c[1] == numero_conta:
                    conta_encontrada = c
                    break
            
            if conta_encontrada:
                saldo, extrato = conta_encontrada[3], conta_encontrada[4]
                contas.extrato(saldo, extrato=extrato)
            else:
                print("Conta não encontrada!")

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
