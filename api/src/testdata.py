from faker import Faker
import random

fake = Faker()

# -------------------------
# GET /posts
# -------------------------
VALID_POST_IDS = ["1", "2", "3"]

INVALID_IDS = [
    "9999",   # inexistente
    "0",      # fora do range
    "-1",     # negativo
    "abc",    # string
    "null",   # literal "null"
]

INVALID_ROUTES = [
    "/postsss/1",
    "/wrong",
    "/posts/%",  # caractere especial quebra rota
]

# -------------------------
# POST /posts
# -------------------------
def make_valid_post():
    return {
        "title": fake.sentence(nb_words=6),
        "body": fake.paragraph(nb_sentences=3),
        "userId": random.randint(1, 10),
    }

# Casos inválidos (para APIs reais, o esperado seria 4xx; no JSONPlaceholder volta 404)
INVALID_PAYLOADS = [
    {"title": 123, "body": True, "userId": "um"},                 # tipos errados
    {"title": ["lista"], "body": {"obj": "x"}, "userId": -5},     # mais tipos errados
    {"title": None, "body": "", "userId": 1},                     # nulos/vazio
    {"body": "sem titulo", "userId": 2},                          # faltando title
    {"title": "sem body", "userId": 3},                           # faltando body
    {"title": "ok", "body": "ok"},                                # faltando userId
]
