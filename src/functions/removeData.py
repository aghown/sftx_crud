def RemoveData(banco:dict):
    teste = True
    while teste == True:
        id = int(input("Qual o ID do usuário que você pretende remover (0 para cancelar)?\n"))
        try:
            if id == "0":
                return None
            else:
                print(banco[id])
                teste = False
        except:
            print("Insira um valor válido")
    while teste == False:
        check = input("Você tem certeza que deseja remover o usuário selecionado? Digite CONFIRMAR para removê-lo ou 0 para cancelar.\n")
        match check:
            case "CONFIRMAR":
                banco.pop(id)
                teste = True
            case "0":
                teste = True
            case __:
                print("Inserção inválida")
                continue