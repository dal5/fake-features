import unittest

import config


class ConfigTest(unittest.TestCase):
    def test_get_crs_bounds_returns_coordinates_for_4326(self):
        run_config = config.Config
        run_config.crs = 4326

        result = run_config.get_crs_bounds(run_config)

        print(result)

        self.assertEquals(result, [[-180.0, -90.0], [180.0, 90.0]])

    def test_get_crs_bounds_fails_if_not_4326(self):
        with self.assertRaises(Exception):
            run_config = config.Config
            run_config.crs = 1234
            run_config.validate_config(self.run_config)

    def test_bbox_within_bounds_passes_validation(self):
        run_config = config.Config
        run_config.crs = 4326
        run_config.bboxMinX = -10
        run_config.bboxMaxX = -10
        run_config.bboxMinY = 0
        run_config.bboxMaxY = 10

        result = run_config.validate_config(run_config)

        self.assertTrue(result)

    def test_bbox_out_of_bounds_fails_validation(self):
        run_config = config.Config
        run_config.crs = 4326
        run_config.bboxMinX = -190

        result = run_config.validate_config(run_config)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
