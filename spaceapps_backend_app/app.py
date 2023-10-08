import uuid
from typing import Annotated

from fastapi import FastAPI, UploadFile, Form, Depends
from fastapi.staticfiles import StaticFiles
from dependency_injector.wiring import inject, Provide
from starlette.background import BackgroundTasks
from starlette.responses import HTMLResponse

from spaceapps_backend_app.algorithm.algorithm import process_image_sequence
from spaceapps_backend_app.cache.container import Container
from spaceapps_backend_app.cache.services import Service

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def main():
    content = """
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
    </head>
    <body>
    <h1>AstroSonix Backend Demo<h1> 
    <form action="/process" enctype="multipart/form-data" method="post">
    Upload image sequence <br />
    <input name="uploaded_images" type="file" multiple /> <br />
    Enter composer name or movie title with great soundtrack <br />
    <input name="composer_or_soundtrack" type="text" /> <br />
    <button type="submit">Generate music</button> <br />
    </form>
    </body>
    """
    return HTMLResponse(content=content)


@app.post("/process")
@inject
async def request_image_sequence_processing_from_scratch(
    background_tasks: BackgroundTasks,
    composer_or_soundtrack: Annotated[str, Form()],
    uploaded_images: list[UploadFile],
    service: Service = Depends(Provide[Container.service]),
):
    request_id = str(uuid.uuid4())
    background_tasks.add_task(
        process_image_sequence,
        request_id,
        composer_or_soundtrack,
        uploaded_images,
        service,
    )

    return {
        "message": f"Go to /process/{request_id} to download a song",
        "request_id": request_id,
    }


@app.get("/process/{request_id}")
@inject
async def request_image_sequence_processing_from_scratch(
    request_id: str, service: Service = Depends(Provide[Container.service])
):
    music = await service.get_music(request_id)

    if music is None:
        return {"message": "Song not ready yet. Please keep refreshing", "ready": False}

    return music


# redis init
container = Container()
container.config.redis_host.from_env("REDIS_HOST", "redis")
container.wire(modules=[__name__])
