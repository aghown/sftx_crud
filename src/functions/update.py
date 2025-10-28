class Empreendedor:
    def __init__(self, id_, nome, email, telefone):
        self.id = id_
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def atualizar(self, nome=None, email=None, telefone=None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone


def atualizar_empreendedor(empreendedores):
    print("\n--- Atualizar Empreendedor ---")
    try:
        id_ = int(input("Informe o ID do empreendedor a ser atualizado: "))
        if id_ not in empreendedores:
            print("ID não encontrado.")
            return

        empreendedor = empreendedores[id_]
        print("\nEmpreendedor encontrado! Deixe em branco para manter o valor atual.")

        novo_nome = input(f"Nome atual: {empreendedor.nome} → Novo: ")
        novo_email = input(f"Email atual: {empreendedor.email} → Novo: ")
        novo_telefone = input(f"Telefone atual: {empreendedor.telefone} → Novo: ")

        empreendedor.atualizar(
            nome=novo_nome if novo_nome.strip() else None,
            email=novo_email if novo_email.strip() else None,
            telefone=novo_telefone if novo_telefone.strip() else None
        )

        print("\nEmpreendedor atualizado com sucesso!")

    except ValueError:
        print("ID inválido.")
