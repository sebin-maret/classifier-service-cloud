from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck(request: Request):
    startup = False
    if request.app.state.startup_completed:
        startup = True
    return {"message": "Hello World", "startup_completed": startup}
