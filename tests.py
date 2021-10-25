import unittest
from app import cuboid_volume

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertAlmostEqual(cuboid_volume(5.5),166.375)

    def test_input_type(self):
        # returns true if TypeError is raised
        self.assertRaises(TypeError, cuboid_volume, l = "10")
            

if __name__ == "__main__":
    unittest.main()