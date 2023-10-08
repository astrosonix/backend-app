from fastapi import UploadFile

from spaceapps_backend_app.algorithm.describe_image import describe_image
from spaceapps_backend_app.algorithm.generate_music import generate_music
from spaceapps_backend_app.cache.services import Service

SOUND_LENGTH = 12  # seconds


async def process_image_sequence(
    request_id: str,
    composer_or_soundtrack: str,
    uploaded_images: list[UploadFile],
    service: Service,
):
    """
    1. Scale down image
    2. Ask AI (time consuming)
    3. Get OpenCV
    4. Merge output
    5. Generate music, return when they are switching

    :param composer_id:
    :param soundtrack_id:
    :param images:
    :return:
    """

    sequence_size = len(uploaded_images)

    # image_descriptions = []
    # for uploaded_image in uploaded_images:
    #     img = await uploaded_image.read()
    #     image_descriptions.append(
    #         describe_image(img, composer_or_soundtrack)
    #     )

    # music = generate_music(image_descriptions)
    music = bytes()

    await service.set_music(request_id, music)
