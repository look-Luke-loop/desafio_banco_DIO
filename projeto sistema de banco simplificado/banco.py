from ast import Break


saldo = 0.0
LIMITE_SAQUE = 3
extrato = []
a = 1
saque_hoje = 0

menu = '''
******MENU******
1 - SALDO
2 - DEPOSITAR
3 - SACAR
4 - EXTRATO
5 - SAIR
****************
'''

while(a != 0):
    option = int(input(menu))

    if option == 1:
        print(f"Seu saldo é: {saldo}");
    
    elif option == 2:
        print("Depositar!");
        deposito = float(input("Digite o valor do depósito: R$ "));
        saldo += deposito;
        extrato.append(deposito*1);
        print(f"Seu novo saldo é R${saldo}");

    elif option == 3:
        print("Sacar!")
        saque = float(input("Digite o valor do saque: R$ "));
        if (saque > saldo):
            print(f"SALDO INSUFICIENTE!\n DEPOSITE MAIS DINHEIRO OU \n SAQUE MENOS DINHEIRO! \n SEU SALDO É: R$ {saldo}");
        elif saque_hoje >= LIMITE_SAQUE:
            print("LIMITE DIÁRIO ATINGIDO. TENTE NOVAMENTE APÓS 00:00H !!!");
            break;
        elif (saque <= saldo) and (saque_hoje < LIMITE_SAQUE):
            print("SAQUE CONCLUÍDO");
            saldo -= saque;
            extrato.append(saque*(-1));
            saque_hoje += 1;
            print(f"saques hoje: {saque_hoje}");

    elif option == 4:
        print("SEU EXTRATO: \n");
        print(extrato,"\n");
    elif option == 5:
        print("SAINDO!")
        break;