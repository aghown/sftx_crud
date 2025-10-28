def ListData(empreendedores: dict):
    """Lista todos os empreendedores cadastrados no banco de dados em memória."""
    
    if not empreendedores:
        print("\n❌ Nenhum empreendedor cadastrado.")
        return
    
    print("\n" + "="*60)
    print("📋 LISTA DE EMPREENDEDORES CADASTRADOS")
    print("="*60)
    
    for id_, empreendedor in empreendedores.items():
        print(f"\n🆔 ID: {id_}")
        print(f"   👤 Nome: {empreendedor.nome}")
        print(f"   🏙️  Cidade: {empreendedor.cidade}")
        print(f"   📧 Email: {empreendedor.email}")
        print(f"   📞 Telefone: {empreendedor.telefone}")
        print(f"   🏢 CNPJ: {empreendedor.cnpj}")
        print(f"   💼 Ramo: {empreendedor.ramo}")
        print("-" * 60)
    
    print(f"\n✅ Total de empreendedores: {len(empreendedores)}")
