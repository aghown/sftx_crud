import re
from functions.create import criar_empreendedor
import functions.update as Update
import functions.removeData as Delete
import functions.listData as List
from functions.database import empreendedores, empreendedorobj
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
                id = lista[0]
                nome = lista[1]
                cidade = lista[2]
                email = lista[3]
                contato = lista[4]
                cnpj = lista[5]
                setor = lista[6]
                criar_empreendedor(id, nome, cidade, email, contato, cnpj, setor, empreendedores, empreendedorobj)
            
            case "2":
                Update.atualizar_empreendedor(empreendedores)
            
            case "3":
                Delete.RemoveData(empreendedores)
            
            case "4":
                List.ListData(empreendedores)
            
            case "5":
                Search.BuscaEmpreendedor(empreendedores).buscar()
            
            case "0":
                break
            
            case _:
                print("Escolha uma opção válida")
