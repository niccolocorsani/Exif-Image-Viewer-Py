from pathlib import Path

from PyQt6.QtWidgets import QFileDialog, QWidget

from MyModel import Model
from MyView import View


class Controller():

    def __init__(self):
        self.model = Model()
        self.view = View(self)




    def handleClick(self,buttonName):
        if(buttonName == 'addPhoto'):
            pass





    def openImage(self):
        return self.model.openImage()



