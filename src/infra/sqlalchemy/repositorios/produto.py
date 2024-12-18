from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome, 
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return schemas.ProdutoSimples(
            id=str(db_produto.id),  # Convertendo id para string
            nome=db_produto.nome,
            preco=db_produto.preco
        )

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return [schemas.ProdutoSimples(
            id=str(produto.id),  # Convertendo id para string
            nome=produto.nome,
            preco=produto.preco
        ) for produto in produtos]