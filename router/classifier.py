import shutil

from fastapi import APIRouter, Request, UploadFile, HTTPException

from service.xray_classifier_service import preprocess_image

router = APIRouter(prefix="/classifier", tags=["classifier"])


@router.post("/predict")
async def get_prediction(request: Request, file: UploadFile):
    print(file)
    try:
        with open("./output/" + file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file.file.close()

    app_model = request.app.state.models["service.xray_classifier_service"]
    response = preprocess_image("./output/" + file.filename, app_model)

    return response
