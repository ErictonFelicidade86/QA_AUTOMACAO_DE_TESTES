import os
import requests
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from urllib.parse import urljoin

load_dotenv()

class APIClient:
    """Cliente HTTP para interações com a API."""
    
    def __init__(self, base_url: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url or os.getenv("BASE_URL")
        self.timeout = int(os.getenv("TIMEOUT_SECONDS", timeout))
        if not self.base_url:
            raise ValueError("BASE_URL não configurada")
    
    @property
    def headers(self) -> Dict[str, str]:
        """Headers padrão para requisições."""
        return {"Content-Type": "application/json"}
    
    def _build_url(self, path: str) -> str:
        """Constrói URL completa a partir do path."""
        path = path.lstrip('/')
        return urljoin(f"{self.base_url}/", path)
    
    def get(self, path: str, params: Optional[Dict] = None) -> requests.Response:
        """Realiza requisição GET."""
        url = self._build_url(path)
        return requests.get(
            url, 
            headers=self.headers, 
            params=params, 
            timeout=self.timeout
        )
    
    def post(self, path: str, json: Optional[Dict] = None) -> requests.Response:
        """Realiza requisição POST."""
        url = self._build_url(path)
        return requests.post(
            url, 
            headers=self.headers, 
            json=json, 
            timeout=self.timeout
        )