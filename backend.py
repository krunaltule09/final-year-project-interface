
import eel
from image_captioning import getCaption

eel.init('web')


@eel.expose
def dummy(path):

    filename = path.split('\\')
    image_dir = "./images/"
    filePath = image_dir+filename[-1]
    caption = getCaption(filePath)
    print("generated caption "+caption)

    return caption


eel.start('index.html', size=(1000, 600))
