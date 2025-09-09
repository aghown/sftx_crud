import re
import functions.create as Create
import functions.update as Update
import functions.removeData as Delete
import functions.listData as List
from functions.database import empreendedores
from functions.saveData import AddData as Save
import functions.search as Search



def OpenMenu():
    while True:
        print("O que você deseja fazer?\n" \
            "1 - Adicionar empreendedor\n" \
            "2 - Atualizar empreendedor\n" \
            "3 - Remover empreendedor\n" \
            "4 - Pesquisar lista de empreendedores\n" \
            "5 - Procurar empreendedor\n" \
            "0 - Cancelar")
        choice = input()
        match choice:
            case "1":
                lista = Save()
                nome = lista[0]
                cidade = lista[1]
                contato = lista[2]
                cnpj = lista[3]
                setor = lista[4]
                Create.criar_empreendedor(empreendedores, nome, cidade, contato, cnpj, setor)
            case "2":
                Update.atualizar_empreendedor(empreendedores)
            case "3":
                Delete.RemoveData(empreendedores)
            case "4":
                List.ListData(empreendedores)
            case "5":
                procurado = input("Digite o nome procurado: ")
                Search.procurar_empreendedores(empreendedores, procurado)
            case "0":
                break
            case _:
                print("Escolha uma opção válida")