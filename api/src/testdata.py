from faker import Faker
from typing import Dict, List
from dataclasses import dataclass

fake = Faker()

@dataclass
class PostTestData:
    """Dados de teste para posts."""
    valid_ids: List[str]
    invalid_ids: List[str]
    invalid_routes: List[str]

class PostDataFactory:
    """Factory para criar dados de teste de posts."""
    
    VALID_POST_IDS = ["1", "2", "3"]
    
    INVALID_IDS = [
        "9999",   # ID inexistente
        "0",      # ID fora do range válido
        "-1",     # ID negativo
        "abc",    # String inválida
        "null",   # Literal "null"
    ]
    
    INVALID_ROUTES = [
        "/postsss/1",  # Rota incorreta
        "/wrong",      # Rota inexistente
        "/posts/%",    # Caractere especial que quebra rota
    ]
    
    @staticmethod
    def create_valid_post() -> Dict[str, any]:
        """Cria payload válido para POST /posts."""
        return {
            "title": fake.sentence(nb_words=6),
            "body": fake.paragraph(nb_sentences=3),
            "userId": fake.random_int(min=1, max=10),
        }
    
    @staticmethod
    def create_invalid_payloads() -> List[Dict[str, any]]:
        """Cria payloads inválidos para testes negativos."""
        return [
            {"title": 123, "body": True, "userId": "um"},                 # Tipos errados
            {"title": ["lista"], "body": {"obj": "x"}, "userId": -5},     # Tipos de dados incorretos
            {"title": None, "body": "", "userId": 1},                     # Valores nulos/vazios
            {"body": "sem titulo", "userId": 2},                          # Falta title
            {"title": "sem body", "userId": 3},                           # Falta body
            {"title": "ok", "body": "ok"},                                # Falta userId
        ]

# Instância global para facilitar uso
post_test_data = PostTestData(
    valid_ids=PostDataFactory.VALID_POST_IDS,
    invalid_ids=PostDataFactory.INVALID_IDS,
    invalid_routes=PostDataFactory.INVALID_ROUTES
)