def procurar_empreendedores(lista, nome_procurado):

    try:
        for empreendedor in lista:
            if empreendedor.get("nome", "").lower() == nome_procurado.lower():
                print("✅ O empreendedor foi encontrado:")
                print("-------------------------")

                for chave, valor in empreendedor.items():
                    print(f"{chave.capitalize()}: {valor}")
                return      
        print("❌ Empreendedor não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao procurar o empreendedor: {e}")
