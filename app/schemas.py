from pydantic import BaseModel

class KnowledgeCreate(BaseModel):
    title: str
    content: str

class KnowledgeOut(KnowledgeCreate):
    id: int
    class Config:
        orm_mode = True
