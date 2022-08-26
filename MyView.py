import os

from PyQt6 import QtCore, uic, QtWidgets
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QFileDialog, QWidget, QTableWidgetItem
import webbrowser

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class View(QWidget):

    def __init__(self, controller,model):
        super(View, self).__init__()

        self.model = model
        self.controller = controller
        self.currentImagePath = None
        self.currentExifInfo = {}
        self.currentRotation = 0
        self.listOfPath = []

        uic.loadUi("ui.ui", self)
        self.showMaximized()
        pixmap = QPixmap("./image.png")
        self.labelOfImage.setPixmap(pixmap.scaled(512, 512, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.tabWidget.setCurrentIndex(0)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.resizeColumnsToContents()

        self.generalExifInfo.clicked.connect(lambda: self.getExifInfo('general'))
        self.detailedExifInfo.clicked.connect(lambda: self.getExifInfo('detailed'))
        self.addPhoto.clicked.connect(self.openImage)
        self.previous.clicked.connect(self.renderPreviousImage)
        self.next.clicked.connect(self.renderNextImage)
        self.rotateLeft.clicked.connect(self.leftRotate)
        self.rotateRight.clicked.connect(self.rightRotate)
        self.openMap.clicked.connect(self.openMapPosition)

    def renderPreviousImage(self):
        index = self.listOfPath.index(self.currentImagePath)
        if index != 0:
            pathPrevious = self.listOfPath[index - 1]
            self.renderImage(pathPrevious)

    def renderNextImage(self):
        index = self.listOfPath.index(self.currentImagePath)
        if index + 1 < len(self.listOfPath):
            pathPrevious = self.listOfPath[index + 1]
            self.renderImage(pathPrevious)

    def getExifInfo(self, behavior):

        self.table.setRowCount(0)
        try:
            if behavior == 'general':
                exifData = self.model.imageDic[self.currentImagePath]
                if exifData == {}:
                    self.controller.errorMessage("The image doesn't contain Exif Data")
                    return
            else:
                exifData = self.model.imageExtendedDic[self.currentImagePath]
                if exifData is None:
                    self.controller.errorMessage("The image doesn't contain Exif Data")
                    return
            self.currentExifInfo = exifData
            i = 0

            for key in exifData.keys():
                self.table.insertRow(i)
                self.table.setItem(i, 0, QTableWidgetItem(key))
                self.table.setItem(i, 1, QTableWidgetItem(str(exifData[key])))
                i = i + 1
        except Exception as ex:
            self.controller.errorMessage(str(ex))

    def openImage(self):

        fname = QFileDialog.getOpenFileName(self, "Open File", ROOT_DIR,
                                            "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        self.listOfPath.append(fname[0])
        if fname:
            self.renderImage(fname[0])

    def renderImage(self, pathName):
        pixmap = QPixmap(pathName)
        if pixmap.isNull():
            self.controller.errorMessage('Problem rendering the image')
            return
        self.labelOfImage.setPixmap(pixmap.scaled(512, 512, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.controller.updateDataModel(pathName)
        self.currentImagePath = pathName

    def leftRotate(self):
        self.currentRotation = self.currentRotation - 90
        pixmap = QPixmap(self.currentImagePath)
        pixmap = pixmap.transformed(QTransform().rotate(self.currentRotation))
        scaled = pixmap.scaled(self.labelOfImage.width(), self.labelOfImage.height(),
                               QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.labelOfImage.setPixmap(scaled)

    def rightRotate(self):
        self.currentRotation = self.currentRotation + 90
        pixmap = QPixmap(self.currentImagePath)
        pixmap = pixmap.transformed(QTransform().rotate(self.currentRotation))
        scaled = pixmap.scaled(self.labelOfImage.width(), self.labelOfImage.height(),
                               QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.labelOfImage.setPixmap(scaled)

    def openMapPosition(self):

        self.getExifInfo('detailed')  ## to get current Exif Info
        try:
            positionN = self.convertDMSTodecimal(self.currentExifInfo['GPSInfo'][2])
            positionE = self.convertDMSTodecimal(self.currentExifInfo['GPSInfo'][4])
        except:
            self.controller.errorMessage('The selected image does not have GPS info')
            return
        position = str(positionN) + ',' + str(positionE)
        print(position)
        if (position is not None):
            webbrowser.open_new("https://www.google.com/maps/search/?api=1&query=" + position)
        else:
            self.controller.errorMessage('Problem parsing the position')

    def convertDMSTodecimal(self, value):
        degree, minute, second = value
        return degree + (minute / 60.0) + (second / 3600.0)
