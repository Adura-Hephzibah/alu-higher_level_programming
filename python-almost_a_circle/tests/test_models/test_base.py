#!/usr/bin/python3
"""
Unittest for class Base
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for Base"""
    def test_base_id(self):
        """no comments"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_base_id_increment(self):
        """no comments"""
        b1 = Base()
        self.assertTrue(b1.id, 1)
        b2 = Base()
        self.assertTrue(b2.id, 2)

    """From Python to JSON"""
    def test_to_json_string(self):
        """no comments"""
        lst = [{'id': 12}]
        lst_str = Base.to_json_string(lst)
        self.assertTrue(lst_str, [{"id": 2}])
        self.assertTrue(lst_str, isinstance(lst_str, str))

    def test_none_to_json_string(self):
        """no comments"""
        lt = None
        lt_str = Base.to_json_string(lt)
        self.assertTrue(lt_str, "[]")
        self.assertTrue(lt_str, isinstance(lt_str, str))

    def test_empty_to_json_string(self):
        """no comments"""
        l = dict()
        l_str = Base.to_json_string(l)
        self.assertTrue(l_str, "[]")
        self.assertTrue(l_str, isinstance(l_str, str))

    """From JSON to Python"""
    def test_from_json_string(self):
        """no comments"""
        j_str = '[{ "id": 89 }]'
        j_list = Base.from_json_string(j_str)
        self.assertTrue(j_list, [{"id": 89}])
        self.assertTrue(j_list, isinstance(j_list, list))

    def test_none_from_json_string(self):
        """no comments"""
        js = None
        js_ls = Base.from_json_string(js)
        self.assertEqual(js_ls, [])
        self.assertTrue(isinstance(js_ls, list))

    def test_empty_from_json_string(self):
        """no comments"""
        j = ""
        j_ls = Base.from_json_string(j)
        self.assertEqual(j_ls, [])
        self.assertTrue(isinstance(j_ls, list))

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
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_str_display(self):
        """test"""
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)
        self.assertEqual(str(r3), '[Rectangle] (1) 0/0 - 3/4')

    def test_display(self):
        """tests"""
        with self.assertRaises(ValueError):
            Rectangle(0, 7).display()

        with self.assertRaises(TypeError):
            Rectangle().display()

        r5 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r5.__str__(1)

    def test_create(self):
        """tests"""
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
