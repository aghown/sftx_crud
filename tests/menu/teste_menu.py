import re
import temp.saveData as Save
import temp.updateData as Update
import temp.removeData as Delete
import temp.searchData as Search



def OpenMenu():
    print("O que você deseja fazer?\n" \
          "1 - Adicionar empreendedor\n" \
          "2 - Atualizar empreendedor\n" \
          "3 - Remover empreendedor\n" \
          "4 - Pesquisar empreendedor")
    choice = input()
    match choice:
        case "1":
            Save.AddData(userList)
        case "2":
            Update.UpdateData(userList)
        case "3":
            Delete.RemoveData(userList)
        case "4":
            Search.SearchData(userList)
        case _:
            print("Escolha uma opção válida")
userList = dict()