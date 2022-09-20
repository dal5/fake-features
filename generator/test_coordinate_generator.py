import unittest

import generator.coordinate_generator


class CoordGeneratorTests(unittest.TestCase):
    def test_valid_point_coordinate_floats(self):
        result = generator.coordinate_generator.generate('Point')

        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], float)

    def test_valid_polygon_coordinates_floats(self):
        result = generator.coordinate_generator.generate('Polygon')

        for coordinates in result:
            self.assertIsInstance(coordinates[0][0], float)
            self.assertIsInstance(coordinates[0][1], float)

    def test_valid_linestring_coordinates_floats(self):
        result = generator.coordinate_generator.generate('LineString')

        for coordinates in result:
            self.assertIsInstance(coordinates[0], float)
            self.assertIsInstance(coordinates[1], float)


if __name__ == '__main__':
    unittest.main()
