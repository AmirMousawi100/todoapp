import os

STATUS_CHOICES = (
    (1, ("pdf")),
    (2, ("txt")),
    (3, ("html")),
    (4, ("jpg")),
    (5, ("py")),
    (6, "png"),
)


def handle_uploaded_file(name, file_ext_code, f):
    file_ext = STATUS_CHOICES[int(file_ext_code) - 1][1]
    with open(
        f"C:/Users/Amir/Desktop/MyUpdatedDjangoStuff/first_updated_project/first_updated_project/templates/first_updated_app/uploaded/{name}.{file_ext}",
        "wb+",
    ) as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_pic(name, f):
    with open(
        f"C:/Users/Amir/Desktop/MyUpdatedDjangoStuff/ToDoApp/static/app1/media/{name}.jpg",
        "wb+",
    ) as destination:
        for chunk in f.chunks():
            destination.write(chunk)
