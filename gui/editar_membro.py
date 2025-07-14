# igreja_mvp/gui/editar_membro.py
import customtkinter as ctk
from tkinter import messagebox
import controllers

class TelaEditarMembro(ctk.CTkToplevel):
    def __init__(self, master, membro_id, callback_refresh):
        super().__init__(master)
        self.title("Editar Membro")
        self.geometry("350x300")
        self.membro_id = membro_id
        self.callback_refresh = callback_refresh # Função para atualizar a lista principal

        # Buscar dados atuais do membro para preencher os campos
        membro = controllers.buscar_membro_por_id(self.membro_id)
        if not membro:
            messagebox.showerror("Erro", "Membro não encontrado.")
            self.destroy()
            return
            
        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self, width=300)
        self.entry_nome.insert(0, membro.nome) # Preenche o campo
        self.entry_nome.pack(pady=5)
        
        self.label_tel = ctk.CTkLabel(self, text="Telefone:")
        self.label_tel.pack(pady=5)
        self.entry_tel = ctk.CTkEntry(self, width=300)
        self.entry_tel.insert(0, membro.telefone) # Preenche o campo
        self.entry_tel.pack(pady=5)

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = ctk.CTkEntry(self, width=300)
        self.entry_email.insert(0, membro.email) # Preenche o campo
        self.entry_email.pack(pady=5)

        self.btn_salvar = ctk.CTkButton(self, text="Salvar Alterações", command=self.salvar_alteracoes)
        self.btn_salvar.pack(pady=20)
        
        # Faz com que esta janela fique em foco
        self.grab_set()
        self.transient(master)

    def salvar_alteracoes(self):
        nome = self.entry_nome.get()
        telefone = self.entry_tel.get()
        email = self.entry_email.get()

        if not nome or not email:
            messagebox.showwarning("Campos Obrigatórios", "Nome e Email são obrigatórios.", parent=self)
            return
        
        try:
            controllers.atualizar_membro(self.membro_id, nome, telefone, email)
            messagebox.showinfo("Sucesso", "Membro atualizado com sucesso!", parent=self)
            self.callback_refresh() # Chama a função para atualizar a lista
            self.destroy() # Fecha a janela de edição
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível atualizar o membro.\nErro: {e}", parent=self)