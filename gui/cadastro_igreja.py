# igreja_mvp/gui/cadastro_igreja.py
import customtkinter as ctk
from tkinter import messagebox
import controllers

class TelaCadastroIgreja(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastrar Igreja")
        self.geometry("300x200")

        self.label_nome = ctk.CTkLabel(self, text="Nome da Igreja:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self, width=250)
        self.entry_nome.pack(pady=5)

        self.label_endereco = ctk.CTkLabel(self, text="Endereço:")
        self.label_endereco.pack(pady=5)
        self.entry_endereco = ctk.CTkEntry(self, width=250)
        self.entry_endereco.pack(pady=5)

        self.btn_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar_igreja)
        self.btn_salvar.pack(pady=10)

    def salvar_igreja(self):
        nome = self.entry_nome.get()
        endereco = self.entry_endereco.get()
        if not nome:
            messagebox.showwarning("Campo Obrigatório", "O nome da igreja não pode ser vazio.")
            return
        
        try:
            controllers.cadastrar_igreja(nome, endereco)
            messagebox.showinfo("Sucesso", f"Igreja '{nome}' cadastrada com sucesso!")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar a igreja.\nErro: {e}")