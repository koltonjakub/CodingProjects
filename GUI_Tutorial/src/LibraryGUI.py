from src.DataReader import LibraryDatabase, Book
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel, QPushButton
from typing import List


class BookTableError(Exception):
    def __init__(self, value: str, message: str) -> None:
        super().__init__(message)

        self.value = value
        self.message = message


class BookTable(QWidget):
    def __init__(self, bookList: List[Book]) -> None:
        super().__init__()

        self.buttonBarPosition: int = None
        self.headlinePosition: int = None

        self.titlePos: int = None
        self.subtitlePos: int = None
        self.authorPos: int = None
        self.pricePos: int = None
        self.publisherPos: int = None
        self.storagePos: int = None

        self.bookList = bookList

    def reloadGrid(self) -> None:
        grid = QGridLayout()

        self.buttonBarPosition: int = 0
        self.headlinePosition: int = 1

        self.titlePos: int = 0
        self.subtitlePos: int = 1
        self.authorPos: int = 2
        self.pricePos: int = 3
        self.publisherPos: int = 4
        self.storagePos: int = 5

        grid.addWidget(QPushButton('back'), self.buttonBarPosition, 0)

        titleLbl = QLabel('title')
        subtitleLbl = QLabel('subtitle')
        authorLbl = QLabel('author')
        priceLbl = QLabel('price')
        publisherLbl = QLabel('publisher')
        storageLbl = QLabel('storage')

        grid.addWidget(titleLbl, self.headlinePosition, self.titlePos)
        grid.addWidget(subtitleLbl, self.headlinePosition, self.subtitlePos)
        grid.addWidget(authorLbl, self.headlinePosition, self.authorPos)
        grid.addWidget(priceLbl, self.headlinePosition, self.pricePos)
        grid.addWidget(publisherLbl, self.headlinePosition, self.publisherPos)
        grid.addWidget(storageLbl, self.headlinePosition, self.storagePos)

        for it, book in enumerate(self.bookList):
            titleLbl = QLabel(book.title)
            subtitleLbl = QLabel(book.subtitle if book.subtitle is not None else '')
            authorLbl = QLabel(book.author)
            priceLbl = QLabel(str(book.price))
            publisherLbl = QLabel(book.publisher)
            storageLbl = QLabel(book.storage)

            titleLbl.adjustSize()
            subtitleLbl.adjustSize()
            authorLbl.adjustSize()
            priceLbl.adjustSize()
            publisherLbl.adjustSize()
            storageLbl.adjustSize()

            grid.addWidget(titleLbl, it + self.headlinePosition + 1, self.titlePos)
            grid.addWidget(subtitleLbl, it + self.headlinePosition + 1, self.subtitlePos)
            grid.addWidget(authorLbl, it + self.headlinePosition + 1, self.authorPos)
            grid.addWidget(priceLbl, it + self.headlinePosition + 1, self.pricePos)
            grid.addWidget(publisherLbl, it + self.headlinePosition + 1, self.publisherPos)
            grid.addWidget(storageLbl, it + self.headlinePosition + 1, self.storagePos)

        self.setLayout(grid)

    @property
    def bookList(self) -> List[Book]:
        return self.__bookList

    @bookList.setter
    def bookList(self, value: List[Book]) -> None:
        if not isinstance(value, List):
            raise BookTableError(value=value, message='bookList is not an instance of type List.')

        for elem in value:
            if not isinstance(elem, Book):
                raise BookTableError(value=elem, message='Every element of bookList has to be of type Book.')

        self.__bookList = value

        self.reloadGrid()


class LibraryManager(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.data: LibraryDatabase = LibraryDatabase()

        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Library Manager')
        self.initUI()

    def initUI(self) -> None:
        self.bookTable = BookTable(bookList=self.data.books)
        self.setCentralWidget(self.bookTable)
