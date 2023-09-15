from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# get single todo
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "todo not found"}


# create todo
@app.post("/todo")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "added todo"}

# update todo

# delete todo
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "item deleted"}
    return {"message": "todo not found"}