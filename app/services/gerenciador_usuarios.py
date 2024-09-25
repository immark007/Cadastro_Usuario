from app.models.usuario import Usuario
from app.utils.random_id_generator import generate_random_id

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, idade, email, telefone, endereco):
        if "@" not in email:
            return "Email inválido. Deve conter '@'."
        id_usuario = generate_random_id()
        usuario = Usuario(nome, idade, email, telefone, endereco, id_usuario)
        self.usuarios.append(usuario)
        return "Usuário adicionado com sucesso."

    def listar_usuarios(self):
        return "\n".join(str(usuario) for usuario in self.usuarios)

    def remover_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                self.usuarios.remove(usuario)
                return "Usuário removido com sucesso."
        return "Usuário não encontrado."

    def editar_usuario(self, nome, novo_nome, nova_idade, novo_email, novo_telefone, novo_endereco):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                usuario.nome = novo_nome
                usuario.idade = nova_idade
                usuario.email = novo_email
                usuario.telefone = novo_telefone
                usuario.endereco = novo_endereco
                return "Usuário editado com sucesso."
        return "Usuário não encontrado."
