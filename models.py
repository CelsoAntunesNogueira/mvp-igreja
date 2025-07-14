# igreja_mvp/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Igreja(Base):
    __tablename__ = "igrejas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    endereco = Column(String)

    membros = relationship("Membro", back_populates="igreja")

class Membro(Base):
    __tablename__ = "membros"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    data_cadastro = Column(DateTime, default=datetime.utcnow)
    
    igreja_id = Column(Integer, ForeignKey("igrejas.id"))
    igreja = relationship("Igreja", back_populates="membros")

    endereco = Column(String)
    data_nascimento = Column(DateTime)
    estado_civil = Column(String) # (Solteiro(a), Casado(a), etc.)
    data_batismo = Column(DateTime)
    status = Column(String, default="Ativo") # (Ativo, Inativo, Transferido, Visitante)
    observacoes = Column(String) # Um campo de texto livre para anotações

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="diretor") # Para futura expansão (ex: "pastor", "secretario")
    
    # Um usuário está ligado a UMA igreja
    igreja_id = Column(Integer, ForeignKey("igrejas.id"))
    igreja = relationship("Igreja")