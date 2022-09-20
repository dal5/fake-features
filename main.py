import logging

from config import config
from generator import feature_generator

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    run_config = config.Config
    logging.info("Start FakeFeatures")
    if run_config.validate_config(run_config):
        logging.info('Validate config success')
    else:
        logging.error('Validate config failure')
    out = feature_generator.generate_feature_collection(run_config)

    f = open("geojson.json", "w")
    f.write(out)
    f.close()
    logging.info('Completed')
