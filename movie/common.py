from datetime import datetime
import os

def get_image_path(instance, filename):
    path = 'static/upload' + datetime.now().strftime("/%Y/%m/%d")
    return os.path.join(path, filename)
