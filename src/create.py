# src/create.py

empreendedores = []  # lista global por enquanto, pode virar banco depois

def criar_empreendedor(id, nome, cidade, contato, cnpj, setor):
    empreendedor = {
        "id": id,
        "nome": nome,
        "cidade": cidade,
        "contato": contato,
        "cnpj": cnpj,
        "setor": setor
    }
    empreendedores.append(empreendedor)
    print("\n✅ Empreendedor cadastrado com sucesso!")
    return empreendedor
