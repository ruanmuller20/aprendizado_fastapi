from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List['Produto']
    minhas_vendas: List['Pedido']
    meus_pedidos: List['Pedido']
    
class Produto(BaseModel):
    id: Optional[str] = None
    usuario: User
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: User
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = None
    

app = FastAPI()