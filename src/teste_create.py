from functions.create import criar_empreendedor, empreendedores

# Criando dois empreendedores de teste
criar_empreendedor(1, "Ana Caroline", "Recife", "ana@email.com", "12.345.678/0001-99", "Tecnologia")
criar_empreendedor(2, "Leonardo Silva", "Olinda", "leo@email.com", "98.765.432/0001-11", "Alimentos")

# Mostrar lista
print("\n📋 Lista de empreendedores:")
print(empreendedores)
