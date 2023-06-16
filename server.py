from typing import Annotated

from fastapi import FastAPI, Request, Path, Body
from fastapi.responses import StreamingResponse, Response
from fastapi.templating import Jinja2Templates

from opencv import get_camera, get_camera_image


app = FastAPI()
template = Jinja2Templates(directory='./')


@app.get('/')
def root(request: Request):
    return template.TemplateResponse('index.html', context={'request': request})


@app.get('/test/{importance}')
def test_view(importance: Annotated[int, Path(title="ddddd")]):
    return {"i": importance}


@app.get('/video')
def video():
    return StreamingResponse(get_camera(), media_type="multipart/x-mixed-replace; boundary=PNPframe")


@app.get(
    '/video/capture',
)
def video_capture():
    data = get_camera_image()
    header = {"Content-Disposition": f"attachment; filename=image.jpeg"}
    return Response(content=data.getvalue(), media_type="image/jpeg", headers=header)