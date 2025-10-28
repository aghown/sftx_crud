def remover_empreendedor(empreendedores: dict):
    print("\n--- Remover Empreendedor ---")

    try:
        id_ = int(input("Informe o ID do empreendedor a ser removido (0 para cancelar): "))
    except ValueError:
        print("ID inválido.")
        return

    if id_ == 0:
        print("Remoção cancelada.")
        return
    
    if id_ not in empreendedores:
        print("ID não encontrado.")
        return

    empreendedor = empreendedores[id_]
    print(f"\nSelecionado: {empreendedor.nome} | {empreendedor.email} | {empreendedor.telefone}")

    confirmacao = input("Digite CONFIRMAR para remover ou Enter para cancelar: ")
    if confirmacao.upper() == "CONFIRMAR":
        empreendedores.pop(id_)
        print("\nEmpreendedor removido com sucesso.")
    else:
        print("\nRemoção cancelada.")
