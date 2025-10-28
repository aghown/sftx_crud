def buscar_empreendedor(empreendedores: dict):
    print("\n--- Buscar Empreendedor ---")
    
    try:
        id_ = int(input("Informe o ID para buscar: "))
    except ValueError:
        print("ID inválido.")
        return

    if id_ not in empreendedores:
        print("Empreendedor não encontrado.")
        return

    empreendedor = empreendedores[id_]
    print(f"\nID: {empreendedor.id} | Nome: {empreendedor.nome} | Email: {empreendedor.email} | Telefone: {empreendedor.telefone}")

