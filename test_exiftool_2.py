from exiftool_helper import ExifTool

with ExifTool() as e:
    get_tags = e.get_metadata('esteganografia_tarea.jpg')
    print(get_tags)
    metadata = e.set_metadata('-Comment=prueba','esteganografia_tarea.jpg')
    get_tags = e.get_metadata('esteganografia_tarea.jpg')
    print(get_tags)