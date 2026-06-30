import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.config import DATASET_PATH, ARTIFACTS_DIR


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join(ARTIFACTS_DIR, "train.csv")
    test_data_path = os.path.join(ARTIFACTS_DIR, "test.csv")
    raw_data_path = os.path.join(ARTIFACTS_DIR, "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")

        try:
            # Read dataset
            df = pd.read_csv(DATASET_PATH)
            logging.info("Dataset loaded successfully")

            # Create artifacts directory
            os.makedirs(ARTIFACTS_DIR, exist_ok=True)

            # Save raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset saved")

            # Train-Test Split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save split datasets
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False
            )

            logging.info("Train and Test datasets saved")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    print("Train Data:", train_path)
    print("Test Data:", test_path)