import PIL
from PIL import Image

def convertImage():
    directory = 'imagens/'

    for files in os.listdir(directory):
        if files.endswith(".png"):
            imageAux = Image.open(directory + files.title())
            imageAux = imageAux.convert(mode="L")
            imageAux.save("imagensOut/"+ files)

if __name__ == '__main__':
    convertImage()