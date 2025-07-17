from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

# Чтобы подняться на два уровня вверх по директориям, иначе будет ошибка (No module named 'app')
sys.path.append(str(Path(__file__).parent.parent))

from app.api.hotels import router as hotels_router


app = FastAPI()
app.include_router(hotels_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
