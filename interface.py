import tkinter as tk
from tkinter import messagebox
from gerenciador_usuarios import GerenciadorUsuarios

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Usuários")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.manager = GerenciadorUsuarios()

        self.build_interface()

    def build_interface(self):
        #Título
        title = tk.Label(self.root, text="Gerenciador de Usuários", font=("Arial", 16), bg="#f0f0f0")
        title.pack(pady=10)

        #Campos de entrada
        self.label_nome = tk.Label(self.root, text="Nome:", bg="#f0f0f0")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root, width=30)
        self.entry_nome.pack(pady=5)

        self.label_idade = tk.Label(self.root, text="Idade:", bg="#f0f0f0")
        self.label_idade.pack()
        self.entry_idade = tk.Entry(self.root, width=30)
        self.entry_idade.pack(pady=5)

        #Botões
        self.btn_adicionar = tk.Button(self.root, text="Adicionar Usuário", command=self.adicionar_usuario, width=25, bg="#4CAF50", fg="white")
        self.btn_adicionar.pack(pady=5)

        self.btn_listar = tk.Button(self.root, text="Listar Usuários", command=self.listar_usuarios, width=25, bg="#2196F3", fg="white")
        self.btn_listar.pack(pady=5)

        self.btn_remover = tk.Button(self.root, text="Remover Usuário", command=self.remover_usuario, width=25, bg="#f44336", fg="white")
        self.btn_remover.pack(pady=5)

        self.btn_editar = tk.Button(self.root, text="Editar Usuário", command=self.editar_usuario, width=25, bg="#FFC107", fg="white")
        self.btn_editar.pack(pady=5)

        #Área de Texto para exibir usuários
        self.text_area = tk.Text(self.root, height=10, width=40)
        self.text_area.pack(pady=10)

    def adicionar_usuario(self):
        nome = self.entry_nome.get()
        try:
            idade = int(self.entry_idade.get())
            mensagem = self.manager.adicionar_usuario(nome, idade)
            messagebox.showinfo("Adicionar Usuário", mensagem)
            self.limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")

    def listar_usuarios(self):
        lista = self.manager.listar_usuarios()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, lista)

    def remover_usuario(self):
        nome = self.entry_nome.get()
        if nome:
            mensagem = self.manager.remover_usuario(nome)
            messagebox.showinfo("Remover Usuário", mensagem)
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Nome do usuário não pode estar vazio.")

    def editar_usuario(self):
        nome = self.entry_nome.get()
        novo_nome = self.entry_nome.get()
        try:
            nova_idade = int(self.entry_idade.get())
            mensagem = self.manager.editar_usuario(nome, novo_nome, nova_idade)
            messagebox.showinfo("Editar Usuário", mensagem)
            self.limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()
