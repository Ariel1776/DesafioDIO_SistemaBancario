print("Criando um Sistema Bancário com Python")
limite = float(500.00)
conta = 0.0
valor = 0.0

#deposito ->
    #Sugestão de argumentos: saldo, valor_deposito, extrato
    #Sugestão de retorno: saldo e extrato.
def deposito(valor):
    global conta
    valor = float(input("Por gentileza, digite o valor do depósito: R$"))
    print()
    if valor <= 0.0:
        print("Impossível depositar valor ZERADO,por gentileza, deposite um valor válido")
    else:
        conta = valor
    
#saque -> 
    #Sugestão de argumentos: saldo, _saque, extrato ,limite(500.00), numero_saques, limite_saques(3)
    #Sugestão de retorno: saldo e extrato.
def saque():
    global conta
    print()
    if conta <= 0.0:
        print("Impossível sacar, sua conta está ZERADA. Deposite algo primeiro.")
        print()
    else:
        while True: 
            sacar = float(input("Limite do saque R$500.00 \nVocê escolheu SACAR. Por gentileza, digite o valor do saque: R$"))
            print()
                    
            if sacar <= 0.00:
                print("Por gentileza digitar um valor válido")
                print()
                break
            elif sacar > limite:
                print("Por gentileza digitar um valor menor que o limite")
                print()
                
            else:
                conta = conta-sacar
                print("Valor do saque foi de: R$", sacar)
                print()
                break

#extrato ->
    #Argumentos posicionais: saldo
    #Argumentos nomeados: extrato
def extrato():
    print("Você escolheu EXTRA1TO.\nO valor atual da sua conta é: R$",conta)

while True:
    programa = int(input(" Escolha uma das opções abaixo: \n1 - Depósito \n2 - Saque \n3 - Extrato \n0 - Fechar programa \n"))
    if programa == 1:
        deposito(valor)
    elif programa == 2:
        saque()
    elif programa == 3:
        extrato()
    elif programa == 0:
        break
    else:
        print("Digite um opção valida")