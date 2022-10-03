import json
import logging
import random

from generator import coordinate_generator

logging.basicConfig(level=logging.DEBUG)


def generate_feature(feature_type, coords):
    return {"type": "Feature", "geometry": {"type": feature_type, "coordinates": coords}}


def generate_feature_collection(config):
    features = []
    current_features = 0
    point_count = 0
    polygon_count = 0
    linestring_count = 0

    while config.max_features > current_features:
        rand = random.randint(1, 3)
        if rand == 1:
            geom_type = 'Point'
            point_count += 1
        if rand == 2:
            geom_type = 'Polygon'
            polygon_count += 1
        if rand == 3:
            geom_type = 'LineString'
            linestring_count += 1

        features.append(generate_feature(geom_type, coordinate_generator.generate(geom_type)))
        current_features += 1

    feature_collection = {"type": "FeatureCollection", "features": features}

    logging.info("Generated feature collection with: \n \t" +
                 str(point_count) + " points\n \t" +
                 str(polygon_count) + " polygons\n \t" +
                 str(linestring_count) + " linestrings")

    return json.dumps(feature_collection)
