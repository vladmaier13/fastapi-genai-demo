# FastAPI GenAI Demo (PostgreSQL + OpenAI GPT-3.5)

Acest proiect demonstrează cum să construiești un API cu **FastAPI**, să stochezi date într-o bază de date **PostgreSQL** și să integrezi un model AI extern (**OpenAI GPT-3.5**) pentru generarea de text.

---

## Caracteristici
- **FastAPI** – framework rapid pentru API-uri REST
- **PostgreSQL** – bază de date relațională
- **SQLAlchemy** – ORM pentru interacțiunea cu baza de date
- **OpenAI GPT-3.5** – endpoint de generare text
- **Docker & Docker Compose** – pentru containerizarea aplicației și a bazei de date

---

## Structura proiectului
```
app/
 ├── main.py          # logica principală FastAPI
 ├── database.py      # conexiune DB
 ├── models.py        # modele ORM
 ├── schemas.py       # scheme Pydantic
 ├── crud.py          # funcții CRUD
docker-compose.yml    # containere: FastAPI + PostgreSQL
requirements.txt      # pachete Python necesare
```

---

## Instalare și rulare
### 1. Clonare repository
```bash
git clone https://github.com/<username>/fastapi-genai-demo.git
cd fastapi-genai-demo
```

### 2. Setează variabilele de mediu
Creează un fișier `.env` (nu îl urca pe GitHub):
```
OPENAI_API_KEY=cheia_ta_openai
```

### 3. Rulează aplicația cu Docker
```bash
docker compose up --build
```

---

## Acces API
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Endpointuri
### 1. Knowledge Base
- `POST /knowledge` → adaugă un articol (title, content)
- `GET /knowledge` → listă articole salvate

### 2. Generare text AI
- `POST /genai` → trimite un prompt și primește un text generat:
```json
{
  "prompt": "Scrie un haiku despre AI și programare"
}
```

---

## Tehnologii utilizate
- Python 3.11
- FastAPI
- PostgreSQL
- Docker
- OpenAI GPT-3.5

---

## Avertisment
- **Cheia OpenAI** trebuie păstrată secretă (`.env` + `.gitignore`).
- Planul gratuit OpenAI are limitări – dacă vezi `insufficient_quota`, trebuie să verifici planul de facturare.

---

## Licență
Acest proiect este oferit ca exemplu educațional și poate fi folosit liber.
