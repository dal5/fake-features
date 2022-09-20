import logging

logging.basicConfig(level=logging.DEBUG)


class Config:
    crs = 4326
    bboxMinX = 1
    bboxMaxX = 2
    bboxMinY = 1
    bboxMaxY = 2
    max_features = 100
    polygon_max_complexity = 6
    linestring_max_complexity = 10

    def get_crs_bounds(self):
        if self.crs == 4326:
            return [[-180.0, -90.0], [180.0, 90.0]]
        else:
            raise Exception('Can\'t get bounds for unknown crs: ' + str(self.crs))

    def is_valid_bbox(self):
        crs_bounds = self.get_crs_bounds(self)
        if crs_bounds[0][0] <= self.bboxMinX <= crs_bounds[1][0] \
                and crs_bounds[0][1] <= self.bboxMinY <= crs_bounds[1][1] \
                and crs_bounds[0][0] <= self.bboxMaxX <= crs_bounds[1][0] \
                and crs_bounds[0][1] <= self.bboxMaxY <= crs_bounds[1][1]:
            return True
        else:
            return False

    def is_valid_crs(self):
        if self.crs == 4326:
            return True
        else:
            return False

    def validate_config(self):
        if self.is_valid_crs(self) and self.is_valid_bbox(self):
            return True
        else:
            return False
