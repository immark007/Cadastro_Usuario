class Usuario:
    def __init__(self, nome, idade, email, telefone, endereco, id_usuario):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}, ID: {self.id_usuario}"
