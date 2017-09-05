import math
import unittest
from circle import Circle
class TestCircle(unittest.TestCase):
    def test_init(self):
        c=Circle(2)
        self.assertEqual(c.r,2)
    def test_girth(self):
        c=Circle(2)
        exp=2*math.pi*2
        self.assertEqual(c.girth(),exp)
    def test_area(self):
        c=Circle(2)
        exp=math.pi*2*2
        self.assertEqual(c.area(),exp)
    def test_cylinderArea(self):
        c=Circle(2)
        h=2
        exp=2*math.pi*2*h+2*math.pi*2*2
        self.assertIsNotNone(h)
        self.assertEqual(c.cylinderArea(h),exp)
    def test_cylinderVolume(self):
        c=Circle(2)
        h=2
        exp=math.pi*2*2*h
        self.assertIsNotNone(h)
        self.assertEqual(c.cylinderVolume(h),exp)
if __name__=='__main__':
    unittest.main()
