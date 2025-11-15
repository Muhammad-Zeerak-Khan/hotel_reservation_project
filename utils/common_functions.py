import os

import yaml

from src.custom_exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)


def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("file is not present in the provided path.")
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Config.yaml file loaded successfully!")
            return config

    except Exception as e:
        logger.error("Error while reading the file.")
        raise CustomException("Failed to read YAML file", e)
