# igreja_mvp/auth.py
import bcrypt

def hash_password(password: str) -> bytes:
    """Gera o hash de uma senha."""
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt)

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """Verifica se a senha fornecida corresponde ao hash."""
    password_byte_enc = plain_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password)