from PyQt6.QtWidgets import QMessageBox

from MyView import View

noExif = {'No ExifData': 'No ExifData'}

class Controller(QMessageBox):

    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

        super(QMessageBox, self).__init__()

    def updateDataModel(self, imagePath):
        self.model.updateListOfImages(imagePath)

    def getExifData(self, imagePath):

        exifData = self.model.imageDic[imagePath]
        if exifData == {}:
            self.errorMessage("The image doesn't contain Exif Data")
            return noExif
        return self.model.imageDic[imagePath]

    def getExtendedExifData(self, imagePath):
        exifData = self.model.imageExtendedDic[imagePath]
        if exifData == None:   ## Differnt behavior of the function _getExif
            self.errorMessage("The image doesn't contain Exif Data")
            return noExif
        return self.model.imageExtendedDic[imagePath]

    def errorMessage(self, stringError):
        msgBox = QMessageBox()
        msgBox.setText(stringError)
        msgBox.exec()
