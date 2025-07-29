import os
from openai import OpenAI
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# -----------------------------------------------------
# Database setup
# -----------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/fastapi_demo")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Knowledge(Base):
    __tablename__ = "knowledge"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------------------------------
# Pydantic Schemas
# -----------------------------------------------------
class KnowledgeCreate(BaseModel):
    title: str
    content: str

class KnowledgeOut(KnowledgeCreate):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2

class GenAIRequest(BaseModel):
    prompt: str

# -----------------------------------------------------
# OpenAI Client (modern API)
# -----------------------------------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------------------------------
# FastAPI App
# -----------------------------------------------------
app = FastAPI(title="GenAI OpenAI Demo API")

@app.get("/")
def root():
    return {"message": "API running with OpenAI GPT-3.5"}

# ---------------- Knowledge Base Endpoints ---------------- #
@app.post("/knowledge", response_model=KnowledgeOut)
def add_knowledge(item: KnowledgeCreate, db: Session = Depends(get_db)):
    db_item = Knowledge(title=item.title, content=item.content)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/knowledge", response_model=list[KnowledgeOut])
def list_knowledge(db: Session = Depends(get_db)):
    return db.query(Knowledge).all()

# ---------------- GenAI Endpoint ---------------- #
@app.post("/genai")
def generate_text(request: GenAIRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return {"result": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
