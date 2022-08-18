#!/usr/bin/python3
"""
Unittest for class Base
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base"""
    def test_base_id(self):
        """no comments"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_base_id_increment(self):
        """no comments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
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
