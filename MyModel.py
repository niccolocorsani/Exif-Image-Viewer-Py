import os
import PIL.Image
import PIL.ExifTags

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Model:
    def __init__(self):
        self.exif_name = ""
        self.exif_dimension = ""
        self.imageDic = {}
        self.imageExtendedDic = {}

    def updateListOfImages(self, imagePath):
        self.imageDic[imagePath] = self.getExif(imagePath)
        self.imageExtendedDic[imagePath] = self.getExtendedExif(imagePath)

    @staticmethod
    def getExtendedExif(imagePath):
        try:
            img = PIL.Image.open(imagePath)
            exif = {
                PIL.ExifTags.TAGS[key]: value
                for key, value in img._getexif().items()
                if key in PIL.ExifTags.TAGS
            }
            return exif
        except Exception:
            return None

    @staticmethod
    def getExif(imagePath):
        try:
            img = PIL.Image.open(imagePath)
            exif = {
                PIL.ExifTags.TAGS[key]: value
                for key, value in img.getexif().items()
                if key in PIL.ExifTags.TAGS
            }
            return exif
        except Exception:
            return None

    def fun(self):
        print("dm")


if __name__ == "__main__":
    model = Model()
#  exif = model.getExif(ROOT_DIR+"/ExifImageViewer/test_image.jpeg")
#  print(exif)
# Model.getExif(ROOT_DIR+"/ExifImageViewer/test_image.jpeg")
