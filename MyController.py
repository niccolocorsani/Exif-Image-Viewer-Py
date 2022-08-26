from PyQt6.QtWidgets import QMessageBox

from MyModel import Model
from MyView import View


class Controller(QMessageBox):

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        self.view.show()
        super(QMessageBox, self).__init__()

    def updateDataModel(self, imagePath):
        if imagePath is None:
            self.errorMessage('Problem with path')
            return

        self.model.updateListOfImages(imagePath)


    def errorMessage(self, stringError):
        msgBox = QMessageBox()
        msgBox.setText(stringError)
        msgBox.exec()


