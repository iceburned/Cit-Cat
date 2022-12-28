from PIL import Image


def resizer(img):
    if img:
        # response = HttpResponse(wrapper,content_type=content_type)
        image = Image.open(img)
        for size in image.size:
            if size > 400:
                image.thumbnail((400, 400))
                pass
        return image
