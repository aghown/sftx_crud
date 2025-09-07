import re

def UpdateData(banco:dict):
    natCheck = True
    try:
        id = int(input("Digite o ID do usuário a ser alterado (Ou 0 para cancelar): "))
    except:
        print("Apenas números.")
    if id == 0:
        return None
    while natCheck == True:
        nome = input("Nome alterado (Deixe em branco para não alterar): ")
        if nome == "":
            nome = banco[id]["Nome"]
            natCheck = False
        else:
            checkname = nome.replace(" ", "")
            if checkname.isalpha() == True:
                natCheck = False
            else:
                print("Digite um nome válido")
    natCheck = True
    while natCheck == True:
        cnpj = input("CNPJ alterado (Deixe em branco para não alterar): ")
        if cnpj == "":
            cnpj = banco[id]["CNPJ"]
            natCheck = False
        else:
            cleanCNPJ = re.sub(r'[^a-zA-Z0-9]', '', cnpj)
            if cleanCNPJ.isdigit() == True and len(cleanCNPJ) == 14:
                natCheck = False
            else:
                print("Digite um CNPJ válido")
    natCheck = True
    while natCheck == True:    
        contact = input("Número alterado com DDD (Deixe em branco para não alterar): ")
        if contact == "":
            contact = banco[id]["Contato"]
            natCheck = False
        else:
            cleanContact = re.sub(r'[^a-zA-Z0-9]', '', contact)
            if cleanContact.isdigit() == True and len(cleanContact) == 11:
                natCheck = False
            else:
                print("Digite um número válido")
    natCheck = True
    city = input("Cidade alterada (Deixe em branco para não alterar): ")
    if city == "":
        city = banco[id]["Cidade"]
    email = input("Email alterado (Deixe em branco para não alterar): ")
    if email == "":
        email = banco[id]["Email"]
    sector = input("Digite o setor: ")
    if sector == "":
        sector = banco[id]["Setor"]
    userData = ({"Nome": nome, "CNPJ":cnpj, "Contato": contact, "Cidade": city, "Email": email, "Setor": sector})
    banco.update({id: userData})