from sqlalchemy.orm import Session, joinedload
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
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id
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
            produtos = self.db.query(models.Produto).options(joinedload(models.Produto.usuario)).all()
            return [schemas.Produto(
                id=str(produto.id),  # Convertendo id para string
                nome=produto.nome,
                detalhes=produto.detalhes,
                preco=produto.preco,
                disponivel=produto.disponivel,
                usuario_id=produto.usuario_id if produto.usuario_id is not None else 0,  # Garantindo que usuario_id seja um inteiro válido
                usuario=schemas.Usuario.model_validate({
                    "id": produto.usuario.id,
                    "nome": produto.usuario.nome,
                    "telefone": produto.usuario.telefone,
                    "senha": produto.usuario.senha or ""  # Garantindo que senha seja uma string válida
                }) if produto.usuario else None
            ) for produto in produtos]