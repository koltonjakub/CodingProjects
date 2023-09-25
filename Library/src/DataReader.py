import pydantic as pt
import numpy as np
import json as js
from typing import Optional, List


class StorageFormatError(Exception):
    def __init__(self, value: str, message: str) -> None:
        super().__init__(message)

        self.value = value
        self.message = message


class Book(pt.BaseModel):
    title: str
    author: str
    price: float
    publisher: str
    storage: str
    subtitle: Optional[str] = None

    @classmethod
    @pt.field_validator("storage")
    def storage_valida(cls, value, info: pt.FieldValidationInfo):
        if len(value) != 3:
            raise StorageFormatError(value=value, message="Storage must contain exactly 3 letters.")

        if not np.all([c.isupper() for c in value]):
            raise StorageFormatError(value=value, message="Storage must contain only uppercase letters.")

        return value


class LibraryDatabase:
    def __init__(self):
        try:
            with open('data/books.json', encoding='utf-8') as file:
                data = js.load(file)
                self.books: List[Book] = [Book(**item) for item in data]

        except FileNotFoundError:
            print(f"The file does not exist.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
