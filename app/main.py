from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mini Todo API")

class Todo(BaseModel):
    title: str
    completed: bool = False

todos = []

@app.get("/")
def home():
    return {"message": "Todo API is running"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    item = {"id": len(todos) + 1, **todo.model_dump()}
    todos.append(item)
    return item

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}
