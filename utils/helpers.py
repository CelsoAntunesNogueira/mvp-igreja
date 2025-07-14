# Em utils/helpers.py
import re

def is_valid_email(email: str) -> bool:
    """Verifica se um e-mail tem um formato básico válido."""
    if not email: return False
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email) is not None

def is_valid_phone(phone: str) -> bool:
    """Verifica se o telefone contém apenas números, parênteses e hífens."""
    # Lógica de validação de telefone
    return True # Implementar