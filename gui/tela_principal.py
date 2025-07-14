# CÓDIGO CORRIGIDO

import customtkinter as ctk
# REMOVA AS IMPORTAÇÕES DAQUI:
# from .cadastro_igreja import TelaCadastroIgreja
# from .cadastro_membro import TelaCadastroMembro
# from .listar_membros import TelaListarMembros

class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Painel Principal")
        self.geometry("400x300")
        
        self.label = ctk.CTkLabel(self, text="Bem-vindo!", font=("Arial", 20))
        self.label.pack(pady=20)
        
        self.btn_cad_igreja = ctk.CTkButton(self, text="Cadastrar Nova Igreja", command=self.abrir_cadastro_igreja)
        self.btn_cad_igreja.pack(pady=10)

        self.btn_cad_membro = ctk.CTkButton(self, text="Cadastrar Novo Membro", command=self.abrir_cadastro_membro)
        self.btn_cad_membro.pack(pady=10)

        self.btn_list_membros = ctk.CTkButton(self, text="Listar Membros", command=self.abrir_lista_membros)
        self.btn_list_membros.pack(pady=10)

    def abrir_cadastro_igreja(self):
        # IMPORTE AQUI
        from .cadastro_igreja import TelaCadastroIgreja
        TelaCadastroIgreja(master=self)

    def abrir_cadastro_membro(self):
        # IMPORTE AQUI
        from .cadastro_membro import TelaCadastroMembro
        TelaCadastroMembro(master=self)

    def abrir_lista_membros(self):
        # IMPORTE AQUI
        from .listar_membros import TelaListarMembros
        TelaListarMembros(master=self)