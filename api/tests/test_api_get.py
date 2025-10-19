import pytest
from src.client import APIClient
from src.testdata import post_test_data
from tests.helpers import ResponseValidator

class TestPostsAPI:
    """Testes para endpoint de posts (GET)."""
    
    @pytest.fixture
    def api_client(self):
        """Fixture que fornece cliente API configurado."""
        return APIClient()
    
    def test_get_all_posts(self, api_client, request):
        path = "/posts"
        response = api_client.get(path)
        
        ResponseValidator.assert_status_code(response, 200, path, request=request)  # ✅ Adicionar request
        
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
    
    @pytest.mark.parametrize("post_id", post_test_data.valid_ids)
    def test_get_post_by_valid_id(self, api_client, post_id, request):
        """Deve retornar post específico quando ID é válido."""
        path = f"/posts/{post_id}"
        response = api_client.get(path)
        
        ResponseValidator.assert_status_code(response, 200, path, request=request)  # ✅ Adicionar request
        
        data = response.json()
        assert data["id"] == int(post_id)
        assert all(key in data for key in ["title", "body", "userId"])
    
    @pytest.mark.parametrize("post_id", post_test_data.invalid_ids, 
                           ids=["inexistente", "zero", "negativo", "string", "null"])
    def test_get_post_by_invalid_id(self, api_client, post_id, request):
        """Deve retornar 404 quando ID é inválido."""
        path = f"/posts/{post_id}"
        response = api_client.get(path)
        
        ResponseValidator.assert_status_code(response, 404, path, request=request)  # ✅ Adicionar request
    
    @pytest.mark.parametrize("invalid_path", post_test_data.invalid_routes)
    def test_get_invalid_routes(self, api_client, invalid_path, request):
        """Deve retornar 404 para rotas inválidas."""
        response = api_client.get(invalid_path)
        
        ResponseValidator.assert_status_code(response, 404, invalid_path, request=request)  # ✅ Adicionar request