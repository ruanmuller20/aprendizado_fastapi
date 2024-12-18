from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, User, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

# criar_bd()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db) ):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios')
def criar_usuario(usuario: User, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuario(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
    