import uvicorn
from fastapi import FastAPI
from router import healthcheck, classifier
from util.lifespan_handlers import lifespan
from config.settings import app_settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add Routers here.
app.include_router(healthcheck.router)
app.include_router(classifier.router)

if __name__ == "__main__":
    uvicorn.run(app, host=app_settings.host, port=app_settings.port)
