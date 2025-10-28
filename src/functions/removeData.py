def RemoveData(empreendedores: dict):
    """Remove um empreendedor do banco de dados em memória."""
    
    while True:
        try:
            id_input = input("Qual o ID do usuário que você pretende remover (0 para cancelar)?\n")
            
            if id_input == "0":
                return None
            
            if id_input not in empreendedores:
                print("❌ ID não encontrado. Insira um valor válido.")
                continue
            
            empreendedor = empreendedores[id_input]
            print(f"\n📋 Empreendedor encontrado:")
            print(f"   ID: {empreendedor.id}")
            print(f"   Nome: {empreendedor.nome}")
            print(f"   Cidade: {empreendedor.cidade}")
            print(f"   Email: {empreendedor.email}")
            print(f"   Telefone: {empreendedor.telefone}")
            print(f"   CNPJ: {empreendedor.cnpj}")
            print(f"   Ramo: {empreendedor.ramo}")
            
            while True:
                check = input("\nVocê tem certeza que deseja remover o usuário selecionado? " 
                            "Digite CONFIRMAR para removê-lo ou 0 para cancelar.\n")
                
                if check == "CONFIRMAR":
                    empreendedores.pop(id_input)
                    print("\n✅ Empreendedor removido com sucesso!")
                    return
                elif check == "0":
                    return
                else:
                    print("❌ Inserção inválida. Digite CONFIRMAR ou 0.")
                    
        except Exception as e:
            print(f"❌ Erro: {e}")
            print("Insira um valor válido")
