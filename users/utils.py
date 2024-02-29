import uuid


def image_upload_to(instance, filename):
    return f'images/{uuid.uuid4()}.{"jpg"}'


def _pdf_to_uplaod(prefix, instance, filename):
    unique_filename = f'{instance.username}_{uuid.uuid4()}.{"pdf"}'
    return f"{prefix}/{unique_filename}"


def cv_upload_to(instance, filename):
    return _pdf_to_uplaod("cv", instance, filename)


def resume_upload_to(instance, filename):
    return _pdf_to_uplaod("re", instance, filename)
