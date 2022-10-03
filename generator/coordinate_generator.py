import random
from config import config

config = config.Config


def generate(feature_type):
    if feature_type == 'Point':
        x_coord = random.uniform(config.bbox_min_x, config.bbox_max_x)
        y_coord = random.uniform(config.bbox_min_y, config.bbox_max_y)
        return [x_coord, y_coord]
    if feature_type == 'Polygon':
        current_complexity = 0
        target_complexity = random.randint(4, config.polygon_max_complexity)

        coordinates = []
        starting_x_coord = random.uniform(config.bbox_min_x, config.bbox_max_x)
        starting_y_coord = random.uniform(config.bbox_min_y, config.bbox_max_y)

        coordinates.append([starting_x_coord, starting_y_coord])

        while current_complexity < target_complexity:
            x_coord = random.uniform(coordinates[0][-0], coordinates[0][-0] + random.uniform(0.0001, 0.0009))
            y_coord = random.uniform(coordinates[0][-1], coordinates[0][-1] + random.uniform(0.0001, 0.0009))
            coordinates.append([x_coord, y_coord])
            current_complexity += 1

        return [coordinates]
    if feature_type == 'LineString':
        coordinates = []
        current_complexity = 0
        target_complexity = random.randint(2, config.linestring_max_complexity)

        starting_x_coord = random.uniform(config.bbox_min_x, config.bbox_max_x)
        starting_y_coord = random.uniform(config.bbox_min_y, config.bbox_max_y)

        coordinates.append([starting_x_coord, starting_y_coord])

        while current_complexity < target_complexity:
            x_coord = random.uniform(coordinates[0][-0], coordinates[0][-0] + random.uniform(0.0001, 0.009))
            y_coord = random.uniform(coordinates[0][-1], coordinates[0][-1] + random.uniform(0.0001, 0.009))
            coordinates.append([x_coord, y_coord])
            current_complexity += 1

        return coordinates
