import re

def OpenMenu():
    print("O que você deseja fazer?\n" \
          "1 - Adicionar empreendedor\n" \
          "2 - Atualizar empreendedor\n" \
          "3 - Remover empreendedor")
    choice = input()
    match choice:
        case "1":
            AddData()
        case "2":
            UpdateData()
        case "3":
            RemoveData()
        case _:
            print("Escolha uma opção válida")
userList = dict()
def AddData():
    natCheck = True
    while natCheck == True:
        nome = input("Digite o nome do empreendedor: ")
        checkname = nome.replace(" ", "")
        if checkname.isalpha() == True:
            natCheck = False
        else:
            print("Digite um nome válido")
    natCheck = True
    while natCheck == True:
        cnpj = input("Digite o CNPJ: ")
        cleanCNPJ = re.sub(r'[^a-zA-Z0-9]', '', cnpj)
        if cleanCNPJ.isdigit() == True and len(cleanCNPJ) == 14:
            natCheck = False
        else:
            print("Digite um CNPJ válido")
    natCheck = True
    while natCheck == True:    
        contact = input("Digiteo número para contato com DDD")
        cleanContact = re.sub(r'[^a-zA-Z0-9]', '', contact)
        if cleanContact.isdigit() == True and len(cleanContact) == 11:
            natCheck = False
        else:
            print("Digite um número válido")
    natCheck = True
    city = input("Digite a cidade: ")
    email = input("Digite o email: ")
    sector = input("Digite o setor: ")
    userData = [nome, cnpj, contact, city, email, sector]
    return userData
