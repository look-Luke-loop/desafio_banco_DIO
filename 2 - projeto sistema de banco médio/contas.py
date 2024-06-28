def criar_conta (lista_contas, lista_usuarios, user_cpf):
    if(user_cpf not in lista_usuarios[::][2]):
        print("Seu usuário não foi encontrato! \n Tente novamente após criar um usuário!")
        return 
    #contas lista é uma matriz[n][4] -> agencia, conta, cpf usuário, saldo e [extrato].

    nova_conta = [ "0001", str(lista_contas.len()),str(user_cpf),0,[]]
    lista_usuarios.append(nova_conta);
    return lista_usuarios;

def sacar (*,saldo , valor, extrato, limite_valor, numero_saques, limite_saques):

    if (valor <= saldo) and (numero_saques <= limite_saques) and (saldo <= limite_valor):
        print("Seu saque será feito e acontecerá em breve. Aguarde!");
        saldo -= valor;
        extrato.append(valor * -1);
    
    elif valor > saldo:
        print("Seu saldo é insuficiente!");
        return; 

    elif limite_saques <= numero_saques:
        print("Número de saques por dia excedido. Tente novamente depois da 00:00h");
        return;

    return saldo, extrato;

def depositar (saldo, valor, extrato,/):
    print(f"Você irá agora depositar R$ {valor} na sua conta!");
    saldo += valor;
    extrato.append(valor);
    print(f"Seu Saldo agora é de: R$ {saldo}!");
    
    return saldo, extrato;




def extrato (*, lista_contas, conta):
    saldo = lista_contas[conta][3]
    print(f"Seu saldo é de: R$ {saldo}.seu extrato é:")
    print("\n")
    for transacoes in lista_contas[conta][4]:
        print(f" R$ {transacoes} \n")
    
    return;


