import sys
import PyQt6.QtWidgets
import src.DataReader
import src.DatabaseGUI


if __name__ == "__main__":
    books = src.DataReader.LibraryDatabase()
    print(books.books)

    app = PyQt6.QtWidgets.QApplication(sys.argv)

    window = src.DatabaseGUI.DatabaseMainWindow(books)
    window.show()

    app.exec()
