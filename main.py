# igreja_mvp/main.py
import customtkinter as ctk
from database import init_db
from controllers import criar_admin_inicial_se_necessario
from gui.tela_login import TelaLogin

# Configuração da aparência (opcional, mas recomendado)
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

def main():
    # 1. Inicializa o banco de dados e cria as tabelas se não existirem
    init_db()

    # 2. Cria o usuário admin padrão se for a primeira execução
    criar_admin_inicial_se_necessario()

    # 3. Inicia a interface gráfica com a tela de login
    app = TelaLogin()
    app.mainloop()

if __name__ == "__main__":
    main()