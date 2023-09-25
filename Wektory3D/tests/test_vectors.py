import unittest
import numpy as np

from modules import Vectors


class VectorTest(unittest.TestCase):
    def test__init__(self):
        # python tuple
        vec = Vectors.Vector((1, 4, 1, 9), 'Vectors.Vector name')

        self.assertEqual(vec.coordinates, (1, 4, 1, 9))
        self.assertEqual(vec.name, 'Vectors.Vector name')
        self.assertEqual(type(vec), Vectors.Vector)

        # python list
        vec = Vectors.Vector([1, 4, 1, 9], 'Vectors.Vector name')

        self.assertEqual(vec.coordinates, (1, 4, 1, 9))
        self.assertEqual(vec.name, 'Vectors.Vector name')
        self.assertEqual(type(vec), Vectors.Vector)

        # numpy ndarray
        array = np.array([1, 4, 1, 9])
        vec = Vectors.Vector(array, 'Vectors.Vector name')

        self.assertEqual(vec.coordinates, (1, 4, 1, 9))
        self.assertEqual(vec.name, 'Vectors.Vector name')
        self.assertEqual(type(vec), Vectors.Vector)

    def test__eq__(self):
        eq1 = Vectors.Vector((1, 2, 3), 'vec1')
        eq2 = Vectors.Vector((1, 2, 3), 'vec2')
        notEq = Vectors.Vector((2, 3, 4), 'vec3')

        self.assertTrue(eq1 == eq2)

        self.assertFalse(eq1 == notEq)

    def test__add__(self):
        vec1 = Vectors.Vector((1, 2, 3))
        vec2 = Vectors.Vector((1, 2, 3))

        expectedResult = vec1 + vec2
        self.assertEqual(expectedResult.coords(), (2, 4, 6))

        expectedResult = vec2 + vec1
        self.assertEqual(expectedResult.coords(), (2, 4, 6))

    def test__sub__(self):
        vec1 = Vectors.Vector((1, 2, 3))
        vec2 = Vectors.Vector((1, 2, 3))

        expectedResult1 = vec1 - vec2
        self.assertEqual(expectedResult1.coords(), (0, 0, 0))

        expectedResult2 = vec2 - vec1
        self.assertEqual(expectedResult2.coords(), (0, 0, 0))

        self.assertEqual(expectedResult1.coords(), expectedResult2.coords())

    def test__mul__(self):
        vec1 = Vectors.Vector((1, 2, 3, 4, 5))
        vec2 = Vectors.Vector((2, 4, 6, 8, 10))

        vec1 *= 2

        self.assertEqual(vec1.coords(), vec2.coords())

    def test__rmul__(self):
        vec1 = Vectors.Vector((1, 2, 3, 4, 5))
        vec2 = Vectors.Vector((2, 4, 6, 8, 10))

        vec1 = 2 * vec1

        self.assertEqual(vec1.coords(), vec2.coords())

    def test__getitem__(self):
        coordinates = np.random.rand(6)

        vec = Vectors.Vector(coordinates)

        for i in range(coordinates.shape[0]):
            self.assertEqual(vec[i], coordinates[i])

    def test__setitem__(self):
        insertValues = np.random.randint(low=3, high=10, size=(3,))

        vec = Vectors.Vector((0, 0, 0))

        for i in range(insertValues.shape[0]):
            vec[i] = insertValues[i]
            self.assertEqual(vec[i], insertValues[i])

    def test__str__(self):
        coordinates = (1, 2, 3, 4)
        name = 'Vectors.Vector name'

        vec = Vectors.Vector(coordinates, name)

        expectedResult = f'{name} = {coordinates}'

        self.assertEqual(str(vec), expectedResult)

    def testCoords(self):
        coords = (1, 2, 3)
        vec = Vectors.Vector(coords)

        self.assertEqual(vec.coords(), coords)

    def testLen(self):
        vecs = [
            Vectors.Vector((1,)),
            Vectors.Vector((1, 1)),
            Vectors.Vector((1, 1, 1)),
            Vectors.Vector((1, 1, 1, 1))
        ]

        expectedResults = [
            np.linalg.norm((1,)),
            np.linalg.norm((1, 1)),
            np.linalg.norm((1, 1, 1)),
            np.linalg.norm((1, 1, 1, 1))
        ]

        for vec, result in zip(vecs, expectedResults):
            self.assertEqual(vec.len(), result)

        # python list
        vecs = [
            Vectors.Vector([1]),
            Vectors.Vector([1, 1]),
            Vectors.Vector([1, 1, 1]),
            Vectors.Vector([1, 1, 1, 1])
        ]

        expectedResults = [
            np.linalg.norm([1]),
            np.linalg.norm([1, 1]),
            np.linalg.norm([1, 1, 1]),
            np.linalg.norm([1, 1, 1, 1])
        ]

        for vec, result in zip(vecs, expectedResults):
            self.assertEqual(vec.len(), result)

        # numpy ndarray
        vecs = [
            Vectors.Vector(np.array([1])),
            Vectors.Vector(np.array([1, 1])),
            Vectors.Vector(np.array([1, 1, 1])),
            Vectors.Vector(np.array([1, 1, 1, 1]))
        ]

        expectedResults = [
            np.linalg.norm(np.array([1])),
            np.linalg.norm(np.array([1, 1])),
            np.linalg.norm(np.array([1, 1, 1])),
            np.linalg.norm(np.array([1, 1, 1, 1]))
        ]

        for vec, result in zip(vecs, expectedResults):
            self.assertEqual(vec.len(), result)

    def testDim(self):
        Vectors.Vectors = [
            Vectors.Vector((1,)),
            Vectors.Vector((1, 2)),
            Vectors.Vector((1, 2, 3)),
            Vectors.Vector((1, 2, 3, 4))
        ]

        expectedResults = [1, 2, 3, 4]

        for vec, res in zip(Vectors.Vectors, expectedResults):
            self.assertEqual(vec.dim(), res)

    def testCopyInit(self):
        vec1 = Vectors.Vector((1, 2, 3))
        vec1Copy = Vectors.Vector(vec1)

        self.assertTrue(vec1 == vec1Copy)

        vec2 = Vectors.Vector((1, 2, 3), 'dummy_name')
        vec2Copy = Vectors.Vector(vec2)

        self.assertTrue(vec2 == vec2Copy)
        self.assertEqual(vec2.name, vec2Copy.name)

    def testName(self):
        vec = Vectors.Vector((1,), 'dummy')
        self.assertEqual(vec.name, 'dummy')


class FunctionsTest(unittest.TestCase):
    def testValidateIterable(self):
        # Check for valid arguments
        vec1 = Vectors.Vector((1,))
        vec2 = Vectors.Vector((2, 2))
        vec3 = Vectors.Vector((3, 3, 3))

        # Shallow structures
        vecList = [vec1, vec2, vec3]
        vecTuple = (vec1, vec2, vec3)
        vecNdarray = np.array([vec1, vec2, vec3])

        # Deep structures
        vecList2 = [[vec1, vec2, vec3],
                    [vec1, vec2, vec3],
                    [vec1, vec2, vec3]]
        vecTuple2 = ((vec1, vec2, vec3),
                     (vec1, vec2, vec3),
                     (vec1, vec2, vec3),)
        vecNdarray2 = np.array([[vec1, vec2, vec3],
                                [vec1, vec2, vec3],
                                [vec1, vec2, vec3]])

        # Double deep structures
        vecList3 = [vecList2, vecList2, vecList2]
        vecTuple3 = (vecTuple2, vecTuple2, vecTuple2)
        vecNdarray3 = np.array([vecNdarray2, vecNdarray2, vecNdarray2])

        # List of structures to be validated
        structures = [vecList, vecTuple, vecNdarray,
                      vecList2, vecTuple2, vecNdarray2,
                      vecList3, vecTuple3, vecNdarray3]

        for elem in structures:
            self.assertTrue(Vectors.validateIterable(elem))

        # Check for invalid arguments
        dummy1 = [1]
        dummy2 = ['dummy vec']
        dummy3 = [109]

        # Shallow structures
        vecList = [dummy1, dummy2, dummy3]
        vecTuple = (dummy1, dummy2, dummy3)
        vecNdarray = np.array([dummy1, dummy2, dummy3])

        # Deep structures
        vecList2 = [[dummy1, dummy2, dummy3],
                    [dummy1, dummy2, dummy3],
                    [dummy1, dummy2, dummy3]]
        vecTuple2 = ((dummy1, dummy2, dummy3),
                     (dummy1, dummy2, dummy3),
                     (dummy1, dummy2, dummy3),)
        vecNdarray2 = np.array([[dummy1, dummy2, dummy3],
                                [dummy1, dummy2, dummy3],
                                [dummy1, dummy2, dummy3]])

        # Double deep structures
        vecList3 = [vecList2, vecList2, vecList2]
        vecTuple3 = (vecTuple2, vecTuple2, vecTuple2)
        vecNdarray3 = np.array([vecNdarray2, vecNdarray2, vecNdarray2])

        # List of structures to be validated
        structures = [vecList, vecTuple, vecNdarray,
                      vecList2, vecTuple2, vecNdarray2,
                      vecList3, vecTuple3, vecNdarray3]

        for elem in [vecList, vecTuple, vecNdarray,
                     vecList2, vecTuple2, vecNdarray2,
                     vecList3, vecTuple3, vecNdarray3]:
            try:
                Vectors.validateIterable(elem)

            except Vectors.VectorException:
                self.assertTrue(True)

            else:
                self.assertTrue(False)

    def testSumVectors(self):
        vec1 = Vectors.Vector((1, 1, 1))
        vec2 = Vectors.Vector((1, 1, 1))

        try:
            Vectors.sumVectors(vec1, vec2, name=123)
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        try:
            Vectors.sumVectors(vec1, vec2, initialZero='1231')
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        try:
            Vectors.sumVectors(vec1, vec2, '1231')
        except Vectors.VectorException:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        expected1 = Vectors.Vector((2, 2, 2))
        result1 = Vectors.sumVectors(vec1, vec2)
        self.assertEqual(result1, expected1)
        self.assertEqual(result1.name, '')

        expected2 = 'result2'
        result2 = Vectors.sumVectors(vec1, vec2, name=expected2)
        self.assertEqual(result2.name, 'result2')

        expected3 = Vectors.Vector((3, 3, 3))
        result3 = Vectors.sumVectors(vec1, vec2, initialZero=1)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()
