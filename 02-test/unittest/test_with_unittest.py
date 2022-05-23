# test_with_unittest.py
from unittest import TestCase

def calculate_area_rectangle(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Test_rectangle_func(TestCase):
    def runTest(self):
        rectangle = calculate_area_rectangle(2, 3)
        self.assertEqual(rectangle, 6, "incorrect area")

class TestGetAreaRectangle(TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)
