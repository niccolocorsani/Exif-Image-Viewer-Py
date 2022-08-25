from PyQt6 import QtWidgets
from MyController import Controller
from MyModel import Model
from MyView import View
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    ui = View(controller, model)
    ui.show()
    sys.exit(app.exec())
