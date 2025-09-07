from create import criar_empreendedor, empreendedores
from search import procurar_empreendedores


criar_empreendedor(1, "Ana Caroline", "Recife", "ana@email.com", "12.345.678/0001-99", "Tecnologia")
criar_empreendedor(2, "Leonardo Silva", "Olinda", "leo@email.com", "98.765.432/0001-11", "Alimentos")


print("Teste 1: Procurar 'Ana'")
procurar_empreendedores(empreendedores, "Ana Caroline")  

print("\nTeste 2: Procurar 'João'")
procurar_empreendedores(empreendedores, "João")         
