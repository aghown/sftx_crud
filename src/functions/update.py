

def atualizar_empreendedor(empreendedores):
    print("\n--- Atualizar Empreendedor ---")
    try:
        id_ = int(input("Informe o ID do empreendedor a ser atualizado: "))
        if id_ not in empreendedores:
            print("ID não encontrado.")
            return

        print("\nEmpreendedor encontrado! Deixe em branco para manter o valor atual.")
        empreendedor = empreendedores[id_]

        for campo, valor_atual in empreendedor.items():
            novo_valor = input(f"{campo.capitalize()} atual: {valor_atual} → Novo: ")
            if novo_valor.strip():
                empreendedor[campo] = novo_valor

        print("\nEmpreendedor atualizado com sucesso!")

    except ValueError:
        print("ID inválido.")


