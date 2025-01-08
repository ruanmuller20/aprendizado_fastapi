from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

# criar_bd()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db) ):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', response_model=List[ProdutoSimples])
def listar_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
    