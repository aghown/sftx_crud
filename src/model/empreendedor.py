# arquivo: empreendedor.py

class Empreendedor:
    def __init__(self, id, nome, cidade, email, telefone, cnpj, ramo):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.email = email
        self.telefone = telefone 
        self.cnpj = cnpj
        self.ramo = ramo

    def atualizar(self, nome = None, cidade = None, email = None, telefone = None, cnpj = None, ramo = None):
        if nome:
            self.nome = nome
        if cidade:
            self.cidade = cidade
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone 
        if cnpj:
            self.cnpj = cnpj
        if ramo:
            self.ramo = ramo

    def __str__(self):
        return f"Empreendedor({self.id}, {self.nome}, {self.cidade}, {self.email}, {self.telefone}, {self.cnpj}, {self.ramo})"
