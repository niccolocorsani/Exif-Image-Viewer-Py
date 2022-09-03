from PyQt6 import QtWidgets
from MyController import Controller
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())
