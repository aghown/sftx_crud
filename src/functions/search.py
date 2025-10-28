class BuscaEmpreendedor:
    def __init__(self, lista_empreendedores: list[dict[str, str]]):
        self.lista = lista_empreendedores

    def buscar(self) -> None:
        """Exibe o menu de busca e processa a escolha do usuário."""
        opcoes = {
            "1": ("nome", "Digite o nome do empreendedor"),
            "2": ("cnpj", "Digite o CNPJ (somente números, 14 dígitos)", 14),
            "3": ("contato", "Digite o contato (somente números)")
        }

        while True:
            print("\n🔍 Buscar Empreendedor")
            print("1. Buscar por nome")
            print("2. Buscar por CNPJ")
            print("3. Buscar por contato")
            print("4. Voltar ao menu inicial")

            escolha = input("\nEscolha uma opção: ").strip()

            if escolha == "4":
                break
            elif escolha in opcoes:
                campo, mensagem, *resto = opcoes[escolha]
                tamanho = resto[0] if resto else None
                self._buscar_por(campo, mensagem, tamanho)
            else:
                print("❌ Opção inválida. Tente novamente.")

    def _buscar_por(self, campo: str, mensagem: str, tamanho: int | None = None) -> None:
        """Realiza a busca por um campo específico."""
        while True:
            valor = input(f"\n{mensagem} ou '0' para voltar: ").strip()
            if valor == "0":
                break
            if not valor:
                print("❌ Valor inválido, tente novamente.")
                continue
            if tamanho and len(valor) != tamanho:
                print(f"❌ O valor deve ter exatamente {tamanho} caracteres.")
                continue

            encontrados = [
                emp for emp in self.lista
                if valor.casefold() in str(emp.get(campo, "")).casefold()
            ]

            if encontrados:
                for emp in encontrados:
                    self._exibir_empreendedor(emp)
            else:
                print("❌ Empreendedor não encontrado.")

    def _exibir_empreendedor(self, emp: dict[str, str]) -> None:
        """Exibe os dados de um empreendedor."""
        print("\n✅ Empreendedor encontrado:")
        print("-------------------------")
        for chave, valor in emp.items():
            print(f"{chave.capitalize()}: {valor}")
