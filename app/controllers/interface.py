import tkinter as tk
from tkinter import messagebox
from app.services.gerenciador_usuarios import GerenciadorUsuarios

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador Completo de Usuários")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E2E2E")

        self.manager = GerenciadorUsuarios()

        self.build_interface()

    def build_interface(self):
        #Titulo do projeto (H1)
        title = tk.Label(self.root, text="Cadastro de Usuários", font=("Arial", 18), bg="#2E2E2E", fg="white")
        title.pack(pady=10)

         # Nome
        self.label_nome = tk.Label(self.root, text="Nome:", bg="#2e2e2e", fg="white")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root, width=40, borderwidth=0, highlightthickness=0, relief="flat")
        self.entry_nome.pack(pady=5)

        # Idade
        self.label_idade = tk.Label(self.root, text="Idade:", bg="#2e2e2e", fg="white")
        self.label_idade.pack()
        self.entry_idade = tk.Entry(self.root, width=40, borderwidth=0, highlightthickness=0, relief="flat")
        self.entry_idade.pack(pady=5)

        # Email
        self.label_email = tk.Label(self.root, text="Email:", bg="#2e2e2e", fg="white")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root, width=40, borderwidth=0, highlightthickness=0, relief="flat")
        self.entry_email.pack(pady=5)

        # Telefone
        self.label_telefone = tk.Label(self.root, text="Telefone:", bg="#2e2e2e", fg="white")
        self.label_telefone.pack()
        self.entry_telefone = tk.Entry(self.root, width=40, borderwidth=0, highlightthickness=0, relief="flat")
        self.entry_telefone.pack(pady=5)

        # Endereço
        self.label_endereco = tk.Label(self.root, text="Endereço:", bg="#2e2e2e", fg="white")
        self.label_endereco.pack()
        self.entry_endereco = tk.Entry(self.root, width=40, borderwidth=0, highlightthickness=0, relief="flat")
        self.entry_endereco.pack(pady=5)

        #Buttons para  adicionar, remover, editar, listar e sair do projeto
        self.btn_adicionar = tk.Button(self.root, text="Adicionar Usuário", command=self.adicionar_usuario, width=30, bg="#4CAF50", fg="white")
        self.btn_adicionar.pack(pady=10)

        self.btn_listar = tk.Button(self.root, text="Listar Usuários", command=self.listar_usuarios, width=30, bg="#2196F3", fg="white")
        self.btn_listar.pack(pady=5)

        self.btn_remover = tk.Button(self.root, text="Remover Usuário", command=self.remover_usuario, width=30, bg="#f44336", fg="white")
        self.btn_remover.pack(pady=5)

        self.btn_editar = tk.Button(self.root, text="Editar Usuário", command=self.editar_usuario, width=30, bg="#FFC107", fg="white")
        self.btn_editar.pack(pady=5)

        #Text-box para listar os usuários
        self.text_area = tk.Text(self.root, height=10, width=60)
        self.text_area.pack(pady=10)

    #Métodos para mostrar, listar e adiconar usuarios, junto com tratamento de execption (Possiveis erros)
    def adicionar_usuario(self):
        nome = self.entry_nome.get()
        try:
            idade = int(self.entry_idade.get())
            email = self.entry_email.get()
            telefone = self.entry_telefone.get()
            endereco = self.entry_endereco.get()
            mensagem = self.manager.adicionar_usuario(nome, idade, email, telefone, endereco)
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
            novo_email = self.entry_email.get()
            novo_telefone = self.entry_telefone.get()
            novo_endereco = self.entry_endereco.get()
            mensagem = self.manager.editar_usuario(nome, novo_nome, nova_idade, novo_email, novo_telefone, novo_endereco)
            messagebox.showinfo("Editar Usuário", mensagem)
            self.limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()
