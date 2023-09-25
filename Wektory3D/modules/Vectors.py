from numpy import ndarray, sqrt, sin, cos, arcsin, arctan, deg2rad, int32, int64, float32, float64
from typing import Tuple, List, Union, Iterable

import numpy as np
import types as ty
import matplotlib.pyplot as plt

# Global Alias for real number, both built in and from numpy
RealNumber = Union[int, int32, int64, float, float32, float64]

# Global Alias for Coordinates type
Coordinates = Union[List[RealNumber], Tuple[RealNumber], ndarray[RealNumber]]


class Vector:
    def __init__(self, initial: Union[Coordinates], vectorName: str = ''):
        """
        :param initial: passed initial value, different action based on passed type
        :param vectorName: name of vector
        """

        validateConstructor(initial=initial, vectorName=vectorName)

        if isinstance(initial, Vector):
            self.copyInit(other=initial, name=vectorName)

        if isCoordinates(initial):
            self.coordinates: Coordinates = tuple(initial)
            self.name: str = vectorName

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise VectorException('Both objects must be of type Vector')

        return self.coordinates == other.coords()

    def __add__(self, other):
        """
        :param other: Vector or coordinates to be added
        :return: summed vectors as Vector class instance
        """
        if (not isinstance(other, Vector)) and not (isCoordinates(other)):
            raise VectorException('Only Vector class or Coordinates can be summed with Vector class')

        if isinstance(other, Vector):
            if self.dim() != other.dim():
                raise VectorException("Vectors must be of same dimension")

            newCoordinates = tuple(
                [selfCoord + otherCoord for selfCoord, otherCoord in zip(list(self.coordinates), list(other.coords()))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        if isCoordinates(other):
            if len(self.coordinates) != len(other):
                raise VectorException("Vectors must be of same dimension")

            newCoordinates = tuple(
                [selfCoord + otherCoord for selfCoord, otherCoord in zip(list(self.coordinates), list(other))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        raise VectorException('Unknown exception in __add__')

    def __sub__(self, other):
        """
        :param other: Vector or coordinates to be added
        :return: subtracted vectors as Vector class instance
        """
        if (not isinstance(other, Vector)) and not (isCoordinates(other)):
            raise VectorException('Only Vector class or Coordinates can be summed with Vector class')

        if isinstance(other, Vector):
            if self.dim() != other.dim():
                raise VectorException("Vectors must be of same dimension")

            newCoordinates = tuple(
                [selfCoord - otherCoord for selfCoord, otherCoord in zip(list(self.coordinates), list(other.coords()))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        if isCoordinates(other):
            if len(self.coordinates) != len(other):
                raise VectorException("Vectors must be of same dimension")

            newCoordinates = tuple(
                [selfCoord - otherCoord for selfCoord, otherCoord in zip(list(self.coordinates), list(other))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        raise VectorException('Unknown exception in __add__')

    def __mul__(self, other):
        if not isinstance(other, Vector) and \
                not isinstance(other, (int, float)) and \
                not isCoordinates(other):
            raise VectorException('Vector class can only be multiplied by number, Coordinates or other Vector')

        if isinstance(other, (int, float)):
            newCoordinates = tuple([other * coord for coord in list(self.coordinates)])
            return Vector(initial=newCoordinates, vectorName=self.name)

        if isinstance(other, Vector):
            newCoordinates = tuple([selfCoord * otherCoord for selfCoord, otherCoord in
                                    zip(list(self.coordinates), list(other.coords()))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        if isCoordinates(other):
            newCoordinates = tuple([selfCoord * otherCoord for selfCoord, otherCoord in
                                    zip(list(self.coordinates), list(other))])
            return Vector(initial=newCoordinates, vectorName=self.name)

        raise VectorException('Unknown exception in __mul__')

    def __rmul__(self, other):
        return self * other

    def __getitem__(self, item) -> Union[int, float, int32, int64, float32, float64]:
        """
        :param item: index or indexes of coordinate to be returned
        :return: coordinate or set of coordinates
        """
        if not isinstance(item, int) and not isinstance(item, Tuple) and \
                not isinstance(item, List) and not isinstance(item, ndarray):
            raise VectorException('Index of coordinate must be integer or pair of integers')

        if isinstance(item, int):
            return list(self.coordinates)[item]

        if isinstance(item, List) or isinstance(item, Tuple) or isinstance(item, ndarray) and len(item) == 2:
            return list(self.coordinates)[item[0]: item[1]]

        raise VectorException('Unknown exception if __getitem__')

    def __setitem__(self, key, value):
        if not isinstance(key, (int, int32, int64)):
            raise VectorException('Vector indexes must be integers')

        if not isinstance(key, (int, int32, int64, float, float32, float64)):
            raise VectorException('Coordinates must be of type int or float')

        coordinatesTemp = list(self.coordinates)
        coordinatesTemp[key] = value
        self.coordinates = tuple(coordinatesTemp)

    def __str__(self) -> str:
        return f'{self.name} = {self.coordinates}'

    def coords(self) -> Coordinates:
        return self.coordinates

    def len(self) -> Union[int, int32, int64, float, float32, float64]:
        return np.linalg.norm(self.coordinates)

    def dim(self) -> int:
        return len(self.coordinates)

    def copyInit(self, other, name):
        self.coordinates: Coordinates = other.coordinates
        self.name: str = other.name if name == '' else name


class VectorException(Exception):
    def __init__(self, message: str = 'Vector Exception has been raised'):
        if isinstance(message, str):
            self.message = message
        super().__init__(self.message)


def isCoordinates(elem) -> bool:
    """
    :param elem: passed element
    :return: check whether element is subscript-able, that satisfies Coordinates type
    """
    return isinstance(elem, List) or \
        isinstance(elem, Tuple) or \
        isinstance(elem, ndarray) or \
        isinstance(elem, ty.GeneratorType)


def validateCoordinates(coordinates: Coordinates) -> bool:
    """
    :param coordinates: coordinates passed to the constructor
    :return: True if all passed parameters are valid
    """
    if not isCoordinates(coordinates):
        raise VectorException('Incorrect coordinates type')

    if not all([isinstance(elem, (int, float, int32, int64, float32, float64)) for elem in list(coordinates)]):
        raise VectorException('All coordinates must be real values')

    return True


def validateConstructor(initial: Union[Coordinates, Vector], vectorName: str) -> bool:
    """
    :param initial: value passed to the constructor, different action based on type
    :param vectorName: name of a vector
    :return: True if all passed parameters are valid
    """

    if isinstance(initial, Vector):
        return True  # The constructor has been already checked

    if not isinstance(vectorName, str):
        raise VectorException('Vector name must be of type string')

    if not isCoordinates(initial):
        raise VectorException(
            'Invalid parameters passed to the constructor, must be of type Coordinates or Vector class')

    return validateCoordinates(coordinates=initial)  # Validation of coordinates is needed


def validateIterable(checkedIter: Iterable) -> bool:
    if isinstance(checkedIter, Vector):  # Case: is Vector, then OK
        return True

    if isinstance(checkedIter, str):  # str is iterable, but is not allowed
        raise VectorException('All arguments must be of type Vector or iterables of type Vector')

    if isinstance(checkedIter, Iterable):  # Case: is Iterable
        if all([isinstance(elem, Vector) for elem in checkedIter]):  # Check if contains only instances of class Vector
            return True

    if isinstance(checkedIter, Iterable):  # Case: is Iterable, deep structure
        if all([validateIterable(elem) for elem in checkedIter]):
            return True

    raise VectorException('All arguments must be of type Vector or iterables of type Vector')


def sumVectors(*args: Tuple[Vector], name: str = None, initialZero: float = 0):
    """
    :param args: Takes multiple Vectors or iterable of vectors
    :param name: input name for returned vector
    :param initialZero:
    :return: sum of inputs as instance of Vector
    """

    # Check if name is provided
    if name is not None:
        if not isinstance(name, str):
            raise ValueError('Vector name must be of type string')

    # Check if initialZero is provided correctly
    if not isinstance(initialZero, RealNumber):
        raise ValueError('Initial zero must be real number')

    # Check if is iterable of Vectors
    if not all([isinstance(elem, Vector) for elem in args]):
        raise VectorException('All elements must be of type Vector')

    # Check if all dimensions are the same
    dimension: int = args[0].dim()

    for vector in args:
        if dimension != vector.dim():
            raise VectorException('All Vectors must be of the same dimension')

    # Sum Vectors
    coordinates: Coordinates = tuple(initialZero for i in range(dimension))
    result = Vector(initial=coordinates)

    if name is not None:
        result.name = name

    for vector in args:
        result += vector

    return result
