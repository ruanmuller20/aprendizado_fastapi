from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from typing import List


router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, session: Session = Depends(get_db) ):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.get('/produtos', response_model=List[Produto])
def listar_produto(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.put('/produtos', response_model=Produto)
def atualizar_produto(produto: Produto, session: Session = Depends(get_db) ):
    RepositorioProduto(session).editar(produto)
    return produto

@router.delete('/produtos/{id}')
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return