import uvicorn
from fastapi import FastAPI
from routers import main

app = FastAPI()

app.include_router(main.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000,
                log_level="info", reload=True)
