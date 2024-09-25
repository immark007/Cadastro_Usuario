import random

class Usuario:
    def __init__(self, nome, idade):
        self.id = random.randint(1000, 9999)  # ID aleatório para o usuário
        self.nome = nome.lower()
        self.idade = idade

    def editar(self, novo_nome, nova_idade):
        self.nome = novo_nome.lower()
        self.idade = nova_idade

    def __str__(self):
        return f"ID: {self.id} - Nome: {self.nome.title()} - Idade: {self.idade}"
