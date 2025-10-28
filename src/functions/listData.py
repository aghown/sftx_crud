def listar_empreendedores(empreendedores: dict):
    print("\n--- Lista de Empreendedores ---")

    if not empreendedores:
        print("Nenhum empreendedor cadastrado.")
        return

    for id_, empreendedor in empreendedores.items():
        print(f"ID: {id_} | Nome: {empreendedor.nome} | Email: {empreendedor.email} | Telefone: {empreendedor.telefone}")
