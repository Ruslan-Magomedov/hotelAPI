from fastapi import FastAPI
import uvicorn

from hotels import router as hotels_router


app = FastAPI()
app.include_router(hotels_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
