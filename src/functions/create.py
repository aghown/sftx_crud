import sys
sys.path.append("src")

from model.empreendedor import Empreendedor

def criar_empreendedor(id: str, nome: str, cidade: str, email: str, telefone: str, 
                       cnpj: str, ramo: str, empreendedores: dict, 
                       empreendedorobj: list) -> Empreendedor:
    """Cria e adiciona um Empreendedor à lista em memória."""
    
    empreendedor = Empreendedor(
        id=id,
        nome=nome,
        cidade=cidade,
        email=email,
        telefone=telefone,
        cnpj=cnpj,
        ramo=ramo
    )
    empreendedores[id] = empreendedor
    empreendedorobj.append(empreendedor)
    
    print("\n✅ Empreendedor cadastrado com sucesso!")
    return empreendedor
