#!/usr/bin/python3
"""documented"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestSquare(unittest.TestCase):
    """tests"""


def test_rec(self):
    """test"""
    r1 = Square(20, 2, 3, 1)
    r2 = Square(3, 4)
    self.assertEqual(r1.width, 20)
    self.assertEqual(r1.height, 20)
    self.assertEqual(r1.size, 20)
    self.assertEqual(r1.x, 2)
    self.assertEqual(r1.y, 3)
    self.assertEqual(r1.id, 1)
    self.assertEqual(r2.width, 3)
    self.assertEqual(r2.height, 3)
    self.assertEqual(r2.size, 3)
    self.assertEqual(r2.x, 4)
    self.assertEqual(r2.y, 0)
    self.assertTrue(r2.id, not None)


def test_validation(self):
    """test"""
    with self.assertRaises(TypeError):
        Square(str(1), 2)
    with self.assertRaises(TypeError):
        Square(1, str(2))
    with self.assertRaises(TypeError):
        Square(1, 2, "3")

    with self.assertRaises(ValueError):
        Square(-1, 2, 3, 4)
    with self.assertRaises(ValueError):
        Square(1, -2, 3, 4)
    with self.assertRaises(ValueError):
        Square(1, 2, -3, 4)


def test_area_str_display(self):
    """test"""
    r3 = Square(3)
    self.assertEqual(r3.area(), 9)
    self.assertEqual(str(r3), '[Square] (1) 0/0 - 3')
    with self.assertRaises(TypeError):
        Square(1, 2, "3", 4).display()

    with self.assertRaises(TypeError):
        Square(6, "7").display()
    r5 = Square(2, 3, 4, 5)
    with self.assertRaises(TypeError):
        r5.__str__(1)
    with self.assertRaises(ValueError):
        Square(0).area()


def test_create(self):
    """tests"""
    """returns an instance with all attributes already set"""
    dic = {"size": 3}
    rect = Square.create(**dic)
    self.assertEqual(rect.area(), 9)


def test_to_dictionary(self):
    """tests"""
    r4 = Square(3, 2, 5, 1)
    self.assertEqual(r4.to_dictionary(),
                     {"id": 1, "size": 3, "x": 2, "y": 5})


def test_update(self):
    """tests"""
    r = Square(3, 4,)
    r.update(size=6, x=2, y=3, id=15)
    self.assertEqual(r.area(), 36)
    dic = {'id': 89, 'size': 2, 'x': 3, 'y': 4}
    r.update(**dic)
    self.assertEqual(r.area(), 4)


def test_save_to_file(self):
    """Test save to file"""
    r = Square(7, 2, 8, 99)
    Square.save_to_file([r])
    with open("Square.json", "r") as file:
        self.assertEqual(json.dumps([r.to_dictionary()]), file.read())


def test_none_save_to_file(self):
    """Test save None to file"""
    Square.save_to_file(None)
    with open("Square.json", "r") as f:
        self.assertEqual('[]', f.read())


def test_empty_save_to_file(self):
    """Test save empty list to file"""
    Square.save_to_file([])
    with open("Square.json", "r") as f:
        self.assertEqual('[]', f.read())


def test_load_from_file(self):
    """Test load from file"""
    r = Square(10, 3, 4, 8)
    Square.save_to_file([r])
    rec = Square.load_from_file()
    self.assertEqual(len(rec), 1)
    for item in rec:
        self.assertEqual(str(item), '[Square] (8) 3/4 - 10')


if __name__ == "__main__":
    unittest.main()
