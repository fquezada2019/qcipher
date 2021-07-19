from pyexif import pyexif

image_path = "esteganografia_tarea.jpg"
metadata = pyexif.ExifEditor(image_path)
metadata.getTags()