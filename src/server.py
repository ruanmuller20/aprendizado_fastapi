from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

# criar_bd()

app = FastAPI()

#CORS
origins = ["http://localhost:3000"]
app.middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*']
)


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, session: Session = Depends(get_db) ):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@app.get('/produtos', response_model=List[Produto])
def listar_produto(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@app.put('/produtos', response_model=Produto)
def atualizar_produto(produto: Produto, session: Session = Depends(get_db) ):
    RepositorioProduto(session).editar(produto)
    return produto

@app.delete('/produtos/{id}')
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return


@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


    