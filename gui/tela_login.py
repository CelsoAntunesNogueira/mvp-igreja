# CÓDIGO CORRIGIDO

import customtkinter as ctk
from tkinter import messagebox
import controllers
# REMOVA A IMPORTAÇÃO DAQUI: from .tela_principal import TelaPrincipal

class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão de Igrejas - Login")
        self.geometry("300x200")
        
        self.label_user = ctk.CTkLabel(self, text="Usuário:")
        self.label_user.pack(pady=5)
        self.entry_user = ctk.CTkEntry(self, placeholder_text="admin")
        self.entry_user.pack(pady=5)
        
        self.label_pass = ctk.CTkLabel(self, text="Senha:")
        self.label_pass.pack(pady=5)
        self.entry_pass = ctk.CTkEntry(self, show="*", placeholder_text="admin")
        self.entry_pass.pack(pady=5)
        
        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.fazer_login)
        self.login_button.pack(pady=10)

    def fazer_login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        if controllers.verificar_login(username, password):
            self.destroy() # Fecha a janela de login
            
            # IMPORTE AQUI, DENTRO DO MÉTODO
            from .tela_principal import TelaPrincipal
            
            app_principal = TelaPrincipal()
            app_principal.mainloop()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")