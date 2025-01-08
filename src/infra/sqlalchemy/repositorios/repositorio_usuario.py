from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario:
    def __init__(self, session: Session):
        self.session = session
        
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            senha=usuario.senha,
            telefone=usuario.telefone
        )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return schemas.Usuario.model_validate({
            "id": str(db_usuario.id),
            "nome": db_usuario.nome,
            "telefone": db_usuario.telefone,
            "senha": db_usuario.senha or ""  # Garantindo que senha seja uma string válida
        })
    
    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return [schemas.Usuario.model_validate({
            "id": str(usuario.id),
            "nome": usuario.nome,
            "telefone": usuario.telefone,
            "senha": usuario.senha or ""  # Garantindo que senha seja uma string válida
        }) for usuario in usuarios]
    
    
    def obter(self):
        pass
    
    def remover(self):
        pass        