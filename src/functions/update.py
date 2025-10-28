import sys
sys.path.append("src")
sys.path.append("src\\functions")

from model.empreendedor import Empreendedor

def atualizar_empreendedor(empreendedores: dict):
    """Atualiza um empreendedor existente no banco de dados em memória."""
    
    print("\n--- Atualizar Empreendedor ---")
    
    try:
        id_ = input("Informe o ID do empreendedor a ser atualizado: ")
        
        if id_ not in empreendedores:
            print("❌ ID não encontrado.")
            return
        
        empreendedor = empreendedores[id_]
        
        print("\nEmpreendedor encontrado! Deixe em branco para manter o valor atual.")
        
        novo_nome = input(f"Nome atual: {empreendedor.nome} → Novo: ")
        novo_cidade = input(f"Cidade atual: {empreendedor.cidade} → Novo: ")
        novo_email = input(f"Email atual: {empreendedor.email} → Novo: ")
        novo_telefone = input(f"Telefone atual: {empreendedor.telefone} → Novo: ")
        novo_cnpj = input(f"CNPJ atual: {empreendedor.cnpj} → Novo: ")
        novo_ramo = input(f"Ramo atual: {empreendedor.ramo} → Novo: ")
        
        empreendedor.atualizar(
            nome=novo_nome if novo_nome.strip() else None,
            cidade=novo_cidade if novo_cidade.strip() else None,
            email=novo_email if novo_email.strip() else None,
            telefone=novo_telefone if novo_telefone.strip() else None,
            cnpj=novo_cnpj if novo_cnpj.strip() else None,
            ramo=novo_ramo if novo_ramo.strip() else None
        )
        
        print("\n✅ Empreendedor atualizado com sucesso!")
        
    except ValueError:
        print("❌ ID inválido.")
    except Exception as e:
        print(f"❌ Erro ao atualizar: {e}")
