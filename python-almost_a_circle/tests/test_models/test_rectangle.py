#!/usr/bin/python3
"""
Documented
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests"""
    def test_rec(self):
        """test"""
        r1 = Rectangle(20, 30, 2, 3, 1)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r2.id, not None)

    def test_validation(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
            Rectangle(1, "2")
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4)
            Rectangle(1, -2, 3, 4)
            Rectangle(1, 2, -3, 4)
            Rectangle(1, 2, 3, -4)

    def test_area_str_display(self):
        """test"""
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)
        self.assertEqual(str(r3), '[Rectangle] (1) 0/0 - 3/4')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3", 4)

    def test_create(self):
        """tests"""
        """returns an instance with all attributes already set"""
        dic = {"width": 3, "height": 4}
        rect = Rectangle.create(**dic)
        self.assertEqual(rect.area(), 12)

    def test_to_dictionary(self):
        """tests"""
        r4 = Rectangle(3, 4, 2, 5, 1)
        self.assertEqual(r4.to_dictionary(),
                         {"id": 1, "width": 3, "height": 4, "x": 2, "y": 5})

    def test_update(self):
        """tests"""
        r = Rectangle(3, 4,)
        r.update(width=4, height=5, x=2, y=3, id=15)
        self.assertEqual(r.area(), 20)
        dic = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r.update(**dic)
        self.assertEqual(r.area(), 2)


if __name__ == "__main__":
    unittest.main()
