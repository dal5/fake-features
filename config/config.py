import json
import logging

logging.basicConfig(level=logging.DEBUG)


class Config:
    with open('config/config.json') as config_json:
        config = json.load(config_json)
        config_json.close

    crs = config['crs']
    bbox_min_x = config['bbox_min_x']
    bbox_max_x = config['bbox_max_x']
    bbox_min_y = config['bbox_min_y']
    bbox_max_y = config['bbox_max_y']
    max_features = config['max_features']
    polygon_max_complexity = config['polygon_max_complexity']
    linestring_max_complexity = config['linestring_max_complexity']

    def get_crs_bounds(self):
        if self.crs == 4326:
            return [[-180.0, -90.0], [180.0, 90.0]]
        else:
            raise Exception('Can\'t get bounds for unknown crs: ' + str(self.crs))

    def is_valid_bbox(self):
        crs_bounds = self.get_crs_bounds(self)
        if crs_bounds[0][0] <= self.bbox_min_x <= crs_bounds[1][0] \
                and crs_bounds[0][1] <= self.bbox_min_y <= crs_bounds[1][1] \
                and crs_bounds[0][0] <= self.bbox_max_x <= crs_bounds[1][0] \
                and crs_bounds[0][1] <= self.bbox_max_y <= crs_bounds[1][1]:
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
