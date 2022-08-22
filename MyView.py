
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import pyqtProperty, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QWidget

from MyModel import Model


class View(QWidget):

    valueChanged = pyqtSignal(object)

    def __init__(self,controller):

        self.controller = controller
        self.model = Model()
        super(View, self,).__init__()
        uic.loadUi("ui.ui", self)


        self.register(self.model.fun)



        # self.addPhoto.clicked.connect(lambda : self.controller.handleClick("addPhoto"))
        self.addPhoto.clicked.connect(self.openImage)


    def register(self, slot):
        self.valueChanged.connect(slot)



    def value(self, newval):
        self._value = newval
        self.valueChanged.emit(self.value)

    def openImage(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "/Users",
                                            "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        self.value('ds')
        if fname:
            self.pixmap = QPixmap(fname[0])
            self.labelOfImage.setPixmap(self.pixmap.scaled(512, 512, QtCore.Qt.AspectRatioMode.KeepAspectRatio))



