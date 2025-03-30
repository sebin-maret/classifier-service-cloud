from fastapi import FastAPI
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_handler(app)
    yield
    shutdown_handler(app)


def startup_handler(app: FastAPI) -> None:
    import pkgutil
    import service

    app.state.models={}
    for service in pkgutil.walk_packages(service.__path__, service.__package__ + '.'):
        if not service.ispkg:
            module = __import__(service.name, globals(), locals(), ['*'])
            if hasattr(module, 'load_model'):
                print("Loading Model from : ", service.name, flush=True)
                app.state.models[service.name]= module.load_model()
    app.state.startup_completed = True


def shutdown_handler(app: FastAPI) -> None:
    pass
