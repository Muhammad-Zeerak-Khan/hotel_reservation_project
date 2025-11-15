import os

import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split

from config.paths_config import *
from src.custom_exception import CustomException
from src.logger import get_logger
from utils.common_functions import read_yaml

# Initialize the logger

logger = get_logger(__name__)


# DATA INGESTION CLASS
class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info(
            f"Data Ingestion started with {self.bucket_name} and file {self.file_name}"
        )

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"CSV file succesffully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.info("Error while downloading the file")
            raise CustomException("Failed to download the csv file", e)

    def split_data(self):
        try:
            logger.info("Starting the data split process.")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(
                data, test_size=1 - self.train_test_ratio, random_state=123
            )

            train_data.to_csv(TRAIN_FILE_PATH)
            train_data.to_csv(TEST_FILE_PATH)
            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split the data", e)

    def run(self):
        try:
            logger.info("Starting the data ingestion process")

            self.download_csv_from_gcp()
            self.split_data()

            logger.info("Data Ingestion completed successfully!")

        except Exception as e:
            logger.error(f"CustomException : {str(e)}")


if __name__ == "__main__":
    config_file = read_yaml(CONFIG_PATH)
    data_ingestion_obj = DataIngestion(config_file)
    data_ingestion_obj.run()
