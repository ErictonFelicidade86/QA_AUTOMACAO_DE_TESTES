from pydantic import BaseModel, Field, validator
from typing import Optional

class PostResponse(BaseModel):
    """Schema de resposta para posts."""
    title: str = Field(..., min_length=1, description="Título do post")
    body: str = Field(..., min_length=1, description="Conteúdo do post")
    userId: int = Field(..., gt=0, description="ID do usuário")
    id: int = Field(..., gt=0, description="ID do post")
    
    @validator('title', 'body')
    def validate_string_fields(cls, v):
        """Valida que strings não estão vazias após strip."""
        if isinstance(v, str):
            v = v.strip()
            if not v:
                raise ValueError("Field cannot be empty or whitespace only")
        return v
    
    class Config:
        """Configurações do schema."""
        anystr_strip_whitespace = True
        validate_assignment = True

class PostRequest(BaseModel):
    """Schema de request para criar posts."""
    title: str = Field(..., min_length=1, max_length=200)
    body: str = Field(..., min_length=1)
    userId: int = Field(..., gt=0)
    
    class Config:
        anystr_strip_whitespace = True