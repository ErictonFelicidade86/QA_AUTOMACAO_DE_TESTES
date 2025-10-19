import logging
from typing import Optional, Dict, Any
import requests
import pytest  # Adicionar import

log = logging.getLogger(__name__)

class ResponseValidator:
    """Validador de respostas HTTP para testes."""
    
    @staticmethod
    def assert_status_code(
        response: requests.Response,
        expected_status: int,
        endpoint_path: str,
        request: pytest.FixtureRequest,  # ✅ Adicionar request como parâmetro obrigatório
        *,
        expected_response_data: Optional[Dict[str, Any]] = None,
        attach_response_json: bool = True
    ) -> None:
        """
        Valida status code da resposta e anexa dados ao relatório.
        """
        # ✅ Agora request está disponível
        request.node.expected_text = f"Expected: status={expected_status} for {endpoint_path}"
        
        if expected_response_data is not None:
            request.node.expected_json = expected_response_data
        
        if attach_response_json and ResponseValidator._is_json_response(response):
            try:
                request.node.response_json = response.json()
            except Exception:
                pass
        
        log.info(
            "Endpoint: %s | Expected status: %s | Actual status: %s",
            endpoint_path,
            expected_status,
            response.status_code
        )
        
        assert response.status_code == expected_status, (
            f"Expected: {expected_status} for {endpoint_path} | "
            f"Actual: {response.status_code}"
        )
    
    @staticmethod
    def _is_json_response(response: requests.Response) -> bool:
        """Verifica se a resposta é JSON."""
        content_type = response.headers.get("Content-Type", "")
        return "application/json" in content_type