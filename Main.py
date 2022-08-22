from PyQt6 import  QtWidgets
from MyController import Controller
from MyView import View

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    controller = Controller()

    ui = View(controller)

    ui.show()
    sys.exit(app.exec())