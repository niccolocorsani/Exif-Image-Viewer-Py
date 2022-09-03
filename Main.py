from PyQt6 import QtWidgets
from MyController import Controller
from MyModel import Model
from MyView import View
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())
