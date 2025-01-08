from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    senha: str
    
    class Config:
        from_attributes = True
    

    
class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
    class Config:
        from_attributes = True
    
class ProdutoSimples(BaseModel):
    id: Optional[str] = None
    nome: str
    preco: float
   
    
    class Config:
        from_attributes = True
    
    
class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = None
    
    class Config:
        from_attributes = True
    

app = FastAPI()