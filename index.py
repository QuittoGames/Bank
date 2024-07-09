from data import user
from tool import Find_Login_Users,Find_User
from random import randint
from datetime import date
from time import sleep

#Variveis Globlais
timenow = date.today()
year = timenow.year
str(year)

#Inteface

def MainBTC(name): # Nao Coloque Sua Chave De Verdade Isso e Apenas Um Teste Em Breve Espero Importar Somente o saldo de BTC para registrar no app poren isso n e manda e nen enviado para ninguem fica localmente registrado em sua ram 
    def MainBTCAplication(BTC_user, wallet_user):
        print("_" * 30, "BTC: {}".format(BTC_user),"_" * 30)
        print("_" * 30, "Public Key Wallet: #### ","_" * 30)
        print("1.")
        command = input("Digite Sua Resposta: ")

        if command.lower() == "main" or command.lower() == "m":
            main()
        elif command.lower() == "1":
            main()

    def CreateWalletBTC():
        wallet_user = input('Digite Sua Carteira De BTC:')

        for i in user:
            if i["nome"] == name:
                i["Wallet"] = wallet_user
                MainBTC(name = name)

    for i in user:
        if name == i["nome"]:
            BTC_user = i["BTC"]
            wallet_user = i["Wallet"]
            if wallet_user.strip() == "":
                CreateWalletBTC()
            else:
                MainBTCAplication(BTC_user, wallet_user)
            break
    else:
        print("Erro 0001x Nome não pode ser encontrado no banco de dados. Tente novamente reiniciando o aplicativo")

def Cards(card_bool):
    cards = Find_User(TypeScreth="cards",name = name)
    print(f"Cards: {cards}")
    if card_bool == False:
        print("1. Create Card")
    command = input("Digite Sua Rsposta: ")

    def CreadCard(card_bool):
        minValue = 0 
        maxValeu = 1000000
        newIDcard = randint(minValue,maxValeu)
        for i in user:
            if newIDcard == cards["ID"]:
                newIDcard = (minValue,maxValeu)

        cards["ID"] = newIDcard
        cards["Name"] = name
        cards["Validade"] = year + 5

        print("Cartao Criado Com Susseso!!!")
        Cards(card_bool= True)

    if command.lower() == "1" and not card_bool:
        CreadCard(card_bool)
    elif command.lower() == "main" or command.lower() == "m":
        main()
    else:
        print("Comando Nao Podee Ser Indetificado!")
        Cards(card_bool= False)

def Pix():
    def PixMain():
        namePix = input("Digite O Nome Do Usuario: ")
        for i in user:
            if namePix == i["nome"]:
                idAcont = Find_User(TypeScreth="ID", name=namePix)
                PixUser = input("Digite O ID Do Usuario Para Transferencia: ")

                if Find_User(TypeScreth="ID", name=namePix) == PixUser:
                    Value_Pix = int(input("Digite O Valor: "))
                    
                    # Adiciona o valor na conta do destinatário
                    for j in user:
                        if j["nome"] == namePix:
                            j["BRL"] += Value_Pix
                            break
                    
                    # Subtrai o valor da conta do remetente
                    for j in user:
                        if j["nome"] == name:
                            j["BRL"] -= Value_Pix
                            break
                    
                    print(f"Transferência realizada com sucesso. Novo saldo de {namePix}: {Find_User(TypeScreth='BRL', name=namePix)}")
                    main()
                else:
                    print("ID do usuário não corresponde ao nome do usuário.")
                    Pix()
            else:
                print("Nome Não Pode Ser Identificado (ERRO: 0001x)")
                PixMain()

    if Find_User(TypeScreth="ID", name=name) == "":
        minValue = 0 
        maxValue = 1000000
        newIDAcont = randint(minValue, maxValue)
        for i in user:
            if i["nome"] == name:
                i["ID"] = str(newIDAcont)
                break
        print(f"ID: {newIDAcont}")
        sleep(1)
        PixMain()
    else:
        PixMain()


def Start():
    command = input("Já Possui Conta No Banco?: ")
    if command.lower() == "y":
        Login()
    elif command.lower() == "n": # Em Desenvolvimento
        print("Feature Ainda N foi Criada")
        Start() 
    elif command.lower() == "main":
        main()
    else:
        print("Comando Não Identificado!")
        Start()

def Login():    
    global name 
    name = input("Digite Seu Nome: ")
    senha = input("Digite Sua Senha: ")
    
    if Find_Login_Users(name, senha):  
        print("Login bem-sucedido!")
        main()
    else:
        print("Nome ou Senha Incorretos")
        Login()

def main():
    #print("_" * 80)
    saldo_brl = Find_User(TypeScreth="BRL",name = name)
    saldo_BTC = Find_User(TypeScreth="BTC",name = name)

    print("_" * 30, "BANK", "_" * 35)
    print("_" * 30, "BRL: {}".format(saldo_brl),"_" * 30)
    print("_" * 30, "BTC: {}".format(saldo_BTC),"_" * 30)
    print("_"* 30 , "1. Ver Extrato","_"* 30)
    print("_"* 30 , "2. BTC Wallet" ,"_"* 30)
    print("_"* 30 , "3. Card " ,"_"* 30)
    
    command =  input("Digite Sua Resposta: ")

    if command.lower() == "1":
        print(Find_User(TypeScreth= "extrato" , name= name))
        main()
    elif command.lower() == "2":
        MainBTC(name= name)
    elif command.lower() == "3":
        Cards(card_bool= False)
    elif command.lower() == "4":
        Pix()
    else:
        main()


# Run Code 
if __name__ == "__main__":
    Start()
