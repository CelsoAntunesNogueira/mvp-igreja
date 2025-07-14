# CÓDIGO ATUALIZADO
import customtkinter as ctk
from tkinter import ttk, messagebox
import controllers
# Importação local para evitar ciclo
# from .editar_membro import TelaEditarMembro 

class TelaListarMembros(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Listar e Gerenciar Membros")
        self.geometry("800x500") # Aumentei o tamanho da janela

        # Frame para o seletor de igreja
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=10, padx=10, fill="x")

        self.igrejas = {igreja.nome: igreja.id for igreja in controllers.listar_todas_igrejas()}
        self.igreja_nomes = list(self.igrejas.keys()) if self.igrejas else ["Nenhuma igreja"]
        
        self.label_igreja = ctk.CTkLabel(self.top_frame, text="Selecione a Igreja:")
        self.label_igreja.pack(side="left", padx=5)
        self.option_igreja = ctk.CTkOptionMenu(self.top_frame, values=self.igreja_nomes, command=self.carregar_membros_pela_selecao)
        self.option_igreja.pack(side="left", padx=5)

        # Frame para a tabela
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Nome", "Telefone", "Email"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=250)
        self.tree.column("Telefone", width=120)
        self.tree.column("Email", width=250)
        
        self.tree.pack(fill="both", expand=True)

        # Frame para os botões de ação
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.pack(pady=10, padx=10, fill="x")

        self.btn_editar = ctk.CTkButton(self.action_frame, text="Editar Membro Selecionado", command=self.editar_membro_selecionado)
        self.btn_editar.pack(side="left", padx=10, pady=5)

        self.btn_excluir = ctk.CTkButton(self.action_frame, text="Excluir Membro Selecionado", command=self.excluir_membro_selecionado, fg_color="red", hover_color="#C10000")
        self.btn_excluir.pack(side="left", padx=10, pady=5)

        # Carregar membros da primeira igreja da lista, se houver
        if self.igreja_nomes[0] != "Nenhuma igreja":
            self.carregar_membros_pela_selecao(self.igreja_nomes[0])

    def carregar_membros_pela_selecao(self, nome_igreja: str):
        """Método chamado pelo OptionMenu para carregar membros."""
        self.atualizar_lista()

    def atualizar_lista(self):
        """Limpa e recarrega a lista de membros com base na igreja selecionada."""
        # Limpar tabela antiga
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        nome_igreja_selecionada = self.option_igreja.get()
        if nome_igreja_selecionada not in self.igrejas:
            return

        igreja_id = self.igrejas[nome_igreja_selecionada]
        membros = controllers.listar_membros_por_igreja(igreja_id)

        for membro in membros:
            self.tree.insert("", "end", values=(membro.id, membro.nome, membro.telefone, membro.email))

    def get_selected_member_id(self):
        """Retorna o ID do membro selecionado na tabela, ou None se nenhum for selecionado."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Nenhuma Seleção", "Por favor, selecione um membro na lista.", parent=self)
            return None
        
        item = self.tree.item(selection[0])
        member_id = item['values'][0]
        return member_id
    
    def editar_membro_selecionado(self):
        membro_id = self.get_selected_member_id()
        if membro_id:
            # Importação local para evitar importação circular
            from .editar_membro import TelaEditarMembro
            TelaEditarMembro(master=self, membro_id=membro_id, callback_refresh=self.atualizar_lista)

    def excluir_membro_selecionado(self):
        membro_id = self.get_selected_member_id()
        if membro_id:
            # Mensagem de confirmação
            resposta = messagebox.askyesno(
                "Confirmar Exclusão", 
                "Você tem certeza que deseja excluir este membro?\nEsta ação não pode ser desfeita.",
                parent=self
            )
            if resposta: # Se o usuário clicou em "Sim"
                try:
                    controllers.deletar_membro(membro_id)
                    messagebox.showinfo("Sucesso", "Membro excluído com sucesso!", parent=self)
                    self.atualizar_lista() # Atualiza a lista para remover o membro
                except Exception as e:
                    messagebox.showerror("Erro", f"Não foi possível excluir o membro.\nErro: {e}", parent=self)