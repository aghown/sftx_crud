
def deletar_empreendedor(id)
global empreendedores
for i, e inenumerate(empreendedores):
    if e["id"] == id:
        del empreendedores[I]
        print(f"\n Empreendedor com ID {id}
        deletado com sucesso!")
        return True
        print(f"\n Nenhum Empreendedor encontrado com ID {id}.")
        return False