from fastapi import FastAPI
from routers import task as task_router
from routers import user as user_router

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)