# igreja_mvp/controllers.py
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import auth

def get_db():
    """Função helper para obter uma sessão do banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def criar_admin_inicial_se_necessario():
    """Cria um usuário 'admin' na primeira vez que o sistema é executado."""
    db: Session = next(get_db())
    if not db.query(models.Admin).first():
        hashed_password = auth.hash_password("admin")
        admin_user = models.Admin(username="admin", hashed_password=hashed_password)
        db.add(admin_user)
        db.commit()
        print("Usuário 'admin' inicial criado com a senha 'admin'.")
    db.close()

def verificar_login(username, password):
    db: Session = next(get_db())
    admin = db.query(models.Admin).filter(models.Admin.username == username).first()
    db.close()
    if admin and auth.verify_password(password, admin.hashed_password):
        return True
    return False

def cadastrar_igreja(nome, endereco):
    db: Session = next(get_db())
    nova_igreja = models.Igreja(nome=nome, endereco=endereco)
    db.add(nova_igreja)
    db.commit()
    db.refresh(nova_igreja)
    db.close()
    return nova_igreja

def listar_todas_igrejas():
    db: Session = next(get_db())
    igrejas = db.query(models.Igreja).all()
    db.close()
    return igrejas

def cadastrar_membro(nome, telefone, email, igreja_id, endereco=None):
    db: Session = next(get_db())
    novo_membro = models.Membro(nome=nome, telefone=telefone, email=email, igreja_id=igreja_id, endereco=endereco)
    db.add(novo_membro)
    db.commit()
    db.refresh(novo_membro)
    db.close()
    return novo_membro

# Exemplo de como a listagem mudaria em controllers.py
def listar_membros_por_igreja(igreja_id_do_usuario_logado: int):
    # A função agora recebe o ID da igreja do usuário logado
    db: Session = next(get_db())
    membros = db.query(models.Membro).filter(models.Membro.igreja_id == igreja_id_do_usuario_logado).all()
    db.close()
    return membros

# ... (código existente) ...

def listar_membros_por_igreja(igreja_id):
    db: Session = next(get_db())
    membros = db.query(models.Membro).filter(models.Membro.igreja_id == igreja_id).all()
    db.close()
    return membros

# --- NOVAS FUNÇÕES CRUD ---

def buscar_membro_por_id(membro_id: int):
    """Busca um único membro pelo seu ID."""
    db: Session = next(get_db())
    membro = db.query(models.Membro).filter(models.Membro.id == membro_id).first()
    db.close()
    return membro

def atualizar_membro(membro_id: int, nome: str, telefone: str, email: str):
    """Atualiza os dados de um membro existente."""
    db: Session = next(get_db())
    membro = db.query(models.Membro).filter(models.Membro.id == membro_id).first()
    if membro:
        membro.nome = nome
        membro.telefone = telefone
        membro.email = email
        db.commit()
        db.close()
        return True
    db.close()
    return False

def deletar_membro(membro_id: int):
    """Deleta um membro do banco de dados."""
    db: Session = next(get_db())
    membro = db.query(models.Membro).filter(models.Membro.id == membro_id).first()
    if membro:
        db.delete(membro)
        db.commit()
        db.close()
        return True
    db.close()
    return False