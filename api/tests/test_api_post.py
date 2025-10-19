import pytest
from src.client import APIClient
from src.testdata import PostDataFactory
from tests.schemas import PostResponse, PostRequest
from tests.helpers import ResponseValidator


class TestPostCreationAPI:
    """Testes para criação de posts via POST."""
    
    @pytest.fixture
    def api_client(self):
        """Fornece cliente API configurado."""
        return APIClient()
    
    @pytest.fixture
    def valid_post_payload(self):
        """Fornece payload válido para criação de post."""
        return PostDataFactory.create_valid_post()
    
    def _validate_created_post(self, response_data: dict, expected_payload: dict) -> PostResponse:
        """
        Valida dados do post criado contra payload esperado.
        
        Args:
            response_data: Dados retornados pela API
            expected_payload: Payload enviado na requisição
            
        Returns:
            PostResponse validado
        """
        # Valida schema da resposta
        created_post = PostResponse(**response_data)
        
        # Valida conteúdo
        assert created_post.title == expected_payload["title"]
        assert created_post.body == expected_payload["body"]
        assert created_post.userId == expected_payload["userId"]
        assert created_post.id > 0
        
        return created_post
    
    def test_create_post_successfully(self, api_client, valid_post_payload, request):
        path = "/posts"
        response = api_client.post(path, json=valid_post_payload)
        
        ResponseValidator.assert_status_code(response, 201, path, request, expected_response_data=valid_post_payload)
        
        self._validate_created_post(response.json(), valid_post_payload)
    
    def test_create_post_validates_schema_successfully(self, api_client, valid_post_payload, request):
        """
        Deve validar schema completo da resposta.
        
        Given: Post criado com sucesso
        
        When: Schema é validado
        
        Then: Todos os campos estão corretos
        """
        path = "/posts"
        
        response = api_client.post(path, json=valid_post_payload)
        
        ResponseValidator.assert_status_code(response, 201, path, request)
        
        # Valida schema completo
        created_post = PostResponse(**response.json())
        
        # Valida tipos e constraints
        assert isinstance(created_post.id, int)
        assert isinstance(created_post.userId, int)
        assert isinstance(created_post.title, str)
        assert isinstance(created_post.body, str)
        assert len(created_post.title) > 0
        assert len(created_post.body) > 0

    def test_create_post_invalid_route(self, api_client, request):
        invalid_path = "/postsss"
        response = api_client.post(invalid_path, json={"title": "test"})
        
        ResponseValidator.assert_status_code(response, 400, invalid_path, request, attach_response_json=False)
    
    @pytest.mark.parametrize("payload,description", [
        ({}, "empty_object"),
        (None, "null_payload"),
        ({"title": "apenas título"}, "partial_payload")
    ])
    def test_create_post_invalid_payloads(self, api_client, payload, description, request):
        """
        Deve retornar 400 para payloads inválidos.
        
        Given: Payload inválido
        
        When: POST /posts é executado
        
        Then: Retorna status 400
        """
        path = "/posts"
        
        response = api_client.post(path, json=payload)
        
        ResponseValidator.assert_status_code(response, 400, path, request, expected_response_data=payload, description=description)
        
        # JSONPlaceholder sempre retorna ID mesmo para payloads inválidos
        data = response.json()
        assert "id" in data and isinstance(data["id"], int) and data["id"] > 0
        
        if payload and "title" in payload and "title" in data:
            assert data["title"] == payload["title"]
    
    @pytest.mark.parametrize("invalid_payload", PostDataFactory.create_invalid_payloads())
    def test_create_post_malformed_data_still_creates(self, api_client, invalid_payload, request):
        """
        Não Deve criar post mesmo com dados malformados.
        
        Given: Payload com tipos de dados incorretos
        
        When: POST /posts é executado
        
        Then: Retorna status 400 mas ainda cria com ID
        """
        path = "/posts"
        
        response = api_client.post(path, json=invalid_payload)
        
        ResponseValidator.assert_status_code(response, 400, path, expected_response_data=invalid_payload, request=request)
        
        # JSONPlaceholder comportamento: sempre retorna ID
        data = response.json()
        assert "id" in data and isinstance(data["id"], int) and data["id"] > 0