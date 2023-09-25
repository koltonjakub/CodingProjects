import PyQt6.QtWidgets
from src.DataReader import LibraryDatabase, Book


class DatabaseMainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self, data: LibraryDatabase):
        super().__init__()

        self.data = data

        self.setGeometry(1200, 700, 300, 300)
        self.setWindowTitle('Library Manager')
        self.initUI()

    def initUI(self):
        for book in self.data.books:
            self.label = PyQt6.QtWidgets.QLabel(self)
            self.label.setText(f'książka')
            self.label.adjustSize()
