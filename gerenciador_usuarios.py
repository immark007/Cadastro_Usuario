from usuario import Usuario

class GerenciadorUsuarios:
    def __init__(self):
        self.lista_usuarios = []

    def adicionar_usuario(self, nome, idade):
        try:
            usuario = Usuario(nome, idade)
            self.lista_usuarios.append(usuario)
            return f"Usuário {usuario.nome.title()} cadastrado com sucesso!"
        except Exception as e:
            return f"Erro ao adicionar usuário: {str(e)}"

    def remover_usuario(self, nome):
        for usuario in self.lista_usuarios:
            if usuario.nome == nome.lower():
                self.lista_usuarios.remove(usuario)
                return f"Usuário {nome.title()} removido com sucesso!"
        return f"Usuário {nome.title()} não encontrado."

    def listar_usuarios(self):
        if not self.lista_usuarios:
            return "Nenhum usuário cadastrado."
        return "\n".join([str(usuario) for usuario in self.lista_usuarios])

    def editar_usuario(self, nome, novo_nome, nova_idade):
        for usuario in self.lista_usuarios:
            if usuario.nome == nome.lower():
                usuario.editar(novo_nome, nova_idade)
                return f"Usuário {nome.title()} atualizado para {novo_nome.title()}, {nova_idade} anos."
        return f"Usuário {nome.title()} não encontrado."
