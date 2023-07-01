print("Criando um Sistema Bancário com Python")

limite = float(500.00)
conta = 0.0


while True:
    programa = int(input("1 - Entrar no programa \n0 - Fechar o programa\n"))

    if programa == 1:
        menu = -1
        while menu != 0:
            menu = int(input("1 - Depósito \n2 - Saque \n3 - Extrato \n0 - Fechar o programa\n"))
                        
            if menu == 1:
                depositar = float(input("Você escolheu DEPOSITAR. Por gentileza, digite o valor do depósito: R$"))
                conta = depositar
                
            elif menu == 2: 
                if conta <= 0.0:
                    print("Impossível sacar, sua conta está ZERADA. Deposite algo primeiro.")
                else:
                    while True: 
                        sacar = float(input("Limite do saque R$500.00 \nVocê escolheu SACAR. Por gentileza, digite o valor do saque: R$"))
                    
                        if sacar <= 0.00:
                            print("Por gentileza digitar um valor válido")
                        elif sacar > limite:
                            print("Por gentileza digitar um valor menor que o limite")
                        else:
                            conta = conta-sacar
                            print("Valor do saque foi de: R$", sacar)
                            break  
            elif menu == 3:
                print("Você escolheu EXTRATO.\nO valor atual da sua conta é: R$",conta)
                
            elif menu == 0:
                break
            else:
                print("Digite uma opção válida")  
    
    elif programa == 0:
        print("Obrigada pela atenção!!!")
        break
        
    else:
        print("Digita uma opção válida")
