# Mini Todo API

Small FastAPI CRUD practice project.

## Run
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Endpoints
- GET `/`
- GET `/todos`
- POST `/todos`
- DELETE `/todos/{todo_id}`
