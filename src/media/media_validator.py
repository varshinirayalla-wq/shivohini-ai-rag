import os


def validate_media(metadata):

    media_fields = [
        "image_urls",
        "pdf_urls",
        "presentation_urls",
        "video_urls"
    ]

    for field in media_fields:

        path = metadata.get(field)

        if path:

            if not os.path.exists(path):
                print(f"Warning: Missing media file -> {path}")

    return metadata