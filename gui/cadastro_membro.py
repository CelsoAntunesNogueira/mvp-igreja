# igreja_mvp/gui/cadastro_membro.py
import customtkinter as ctk
from tkinter import messagebox
import controllers
from utils.helpers import is_valid_email


class TelaCadastroMembro(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastrar Membro")
        self.geometry("350x450")
        
        self.igrejas = {igreja.nome: igreja.id for igreja in controllers.listar_todas_igrejas()}
        igreja_nomes = list(self.igrejas.keys()) if self.igrejas else ["Nenhuma igreja cadastrada"]

        self.label_igreja = ctk.CTkLabel(self, text="Igreja:")
        self.label_igreja.pack(pady=5)
        self.option_igreja = ctk.CTkOptionMenu(self, values=igreja_nomes)
        self.option_igreja.pack(pady=5)

        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self, width=300)
        self.entry_nome.pack(pady=5)
        
        self.label_tel = ctk.CTkLabel(self, text="Telefone:")
        self.label_tel.pack(pady=5)
        self.entry_tel = ctk.CTkEntry(self, width=300)
        self.entry_tel.pack(pady=5)

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = ctk.CTkEntry(self, width=300)
        self.entry_email.pack(pady=5)

        self.label_endereco = ctk.CTkLabel(self, text="Endereço:")
        self.label_endereco.pack(pady=5)
        self.entry_endereco = ctk.CTkEntry(self, width=300)
        self.entry_endereco.pack(pady=5)

        self.btn_salvar = ctk.CTkButton(self, text="Salvar Membro", command=self.salvar_membro)
        self.btn_salvar.pack(pady=10)

    def salvar_membro(self):
        nome_igreja_selecionada = self.option_igreja.get()
        if nome_igreja_selecionada == "Nenhuma igreja cadastrada":
            messagebox.showerror("Erro", "Cadastre uma igreja primeiro.")
            return

        igreja_id = self.igrejas[nome_igreja_selecionada]
        nome = self.entry_nome.get()
        telefone = self.entry_tel.get()
        email = self.entry_email.get()
        endereco = self.entry_endereco.get()
        
        if not is_valid_email(email):
            messagebox.showerror("Dado Inválido", "O formato do e-mail é inválido.")
            return # Impede o salvamento

        if not nome or not email:
            messagebox.showwarning("Campos Obrigatórios", "Nome e Email são obrigatórios.")
            return
        
        try:
            controllers.cadastrar_membro(nome, telefone, email, igreja_id, endereco=endereco)
            messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar o membro.\nErro: {e}")

