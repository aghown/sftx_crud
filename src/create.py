from model.empreendedor import Empreendedor
from database import empreendedores   #importa a lista global

def criar_empreendedor(id: int, nome: str, cidade: str, email: str, telefone: str, cnpj: str, ramo: str) -> Empreendedor:
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
    empreendedores.append(empreendedor)
    print("\n✅ Empreendedor cadastrado com sucesso!")
    return empreendedores

