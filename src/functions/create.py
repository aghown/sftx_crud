# src/create.py

#Fiz alteração para receber o banco e o ID ter auto incremento

def criar_empreendedor(empreendedores:dict, nome, cidade, contato, cnpj, setor):
    id = len(empreendedores) + 1
    idcheck = False
    while idcheck == False:
        if empreendedores.__contains__(id):
            id+=1
        else:
            idcheck = True
    empreendedor = {
        "nome": nome,
        "cidade": cidade,
        "contato": contato,
        "cnpj": cnpj,
        "setor": setor
    }
    empreendedores.update({id: empreendedor})
    print("\n✅ Empreendedor cadastrado com sucesso!")
    return empreendedor
