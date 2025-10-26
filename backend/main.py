from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
# from tasks.routes import router as tasks_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
# app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API"}