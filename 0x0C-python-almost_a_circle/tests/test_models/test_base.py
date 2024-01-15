ttest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for the Base Class"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_id(self):
        """Tests id values given"""
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(2), self.id == 2)
        self.assertTrue(Base(-50), self.id == -50)

    def test_id_None(self):
        """Tests if id is not given, __nb_objects is incremented"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test the accessibility for private attributes"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class_name(self):
        """Test class created is Base"""
        self.assertTrue(Base(0), self.__class__ == Base)

    def test_to_json_str(self):
        """Testing the output of the to_json_string func"""
        d1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d2 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        s1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},'
        s2 = ' {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        str1 = Base.to_json_string([d1, d2])
        self.assertTrue(type(str1) == str)
        self.assertEqual(str1, s1 + s2)

    def test_to_json_str_empty(self):
        """Testing the to_json_string func for an empty dict"""
        d = dict()
        strd = Base.to_json_string([d])
        self.assertTrue(len(d) == 0)
        self.assertEqual(strd, "[{}]")

    def test_to_json_str_None(self):
        """Testing the to_json_string func for an None dict"""
        d2 = None
        strd2 = Base.to_json_string([d2])
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

    def test_from_json_str(self):
        """Testing the from_json_string func"""
        s = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        res_list = Base.from_json_string(s)
        d1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d2 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        self.assertTrue(type(res_list) == list)
        self.assertTrue(type(res_list[0]) == dict)
        self.assertEqual(res_list, [d1, d2])

    def test_from_json_str_None(self):
        """Testing the from_json_string func for a None string"""
        s = None
        result = Base.from_json_string(s)
        self.assertEqual(result, [])

    def test_from_json_str_empty(self):
        """Testing the from_json_string func for an empty string"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

    def test_creat(self):
        """Testing the create func"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (2) 1/0 - 3/5')

    def test_save_to_file(self):
        """Testing the save to file func"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r1_dict, r2_dict]), file.read())

    def test_save_to_file_None(self):
        """Testing the save to file func for None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_empty(self):
        """Testing the save to file func for empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        """Testing the load_from_file func"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = Rectangle.load_from_file()
        for k, v in enumerate(res):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (7) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (8) 0/0 - 2/4')

    def test_load_from_file_None(self):
        """Testing the load_from_file func for None"""
        Rectangle.save_to_file(None)
        res = Rectangle.load_from_file()
        self.assertEqual(type(res), list)
        self.assertEqual(len(res), 0)

    def test_load_from_file_empty(self):
        """Testing the load_from_file func for empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)i:WQ
