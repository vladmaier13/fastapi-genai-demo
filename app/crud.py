from sqlalchemy.orm import Session
from . import models, schemas

def create_knowledge(db: Session, knowledge: schemas.KnowledgeCreate):
    db_item = models.Knowledge(title=knowledge.title, content=knowledge.content)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_knowledge(db: Session):
    return db.query(models.Knowledge).all()
