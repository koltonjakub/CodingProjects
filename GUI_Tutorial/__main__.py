import sys
import PyQt6.QtWidgets
import src.LibraryGUI


if __name__ == "__main__":
    app = PyQt6.QtWidgets.QApplication(sys.argv)

    window = src.LibraryGUI.LibraryManager()
    window.show()

    app.exec()
