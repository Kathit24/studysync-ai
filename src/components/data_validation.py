import os
import sys
from dataclasses import dataclass

import pandas as pd

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataValidationConfig:
    validation_report_path = os.path.join(
        "artifacts",
        "validation_report.txt"
    )


class DataValidation:
    def __init__(self):
        self.validation_config = DataValidationConfig()

    def validate_dataset(self, file_path):
        try:
            logging.info("Starting Data Validation")

            df = pd.read_csv(file_path)

            report = []

            # Missing values
            if df.isnull().sum().sum() == 0:
                report.append("No missing values found")
            else:
                report.append("Missing values detected")

            # Duplicate rows
            if df.duplicated().sum() == 0:
                report.append("No duplicate rows found")
            else:
                report.append("Duplicate rows detected")

            # Required columns
            required_columns = [
                "age",
                "gender",
                "semester",
                "study_hours",
                "attendance",
                "assignment_completion",
                "previous_gpa",
                "mock_test_score",
                "sleep_hours",
                "screen_time",
                "stress_level",
                "programming_practice_hours",
                "class_participation",
                "learning_style",
                "final_gpa"
            ]

            missing_columns = [
                col
                for col in required_columns
                if col not in df.columns
            ]

            if len(missing_columns) == 0:
                report.append("All required columns present")
            else:
                report.append(
                    f"Missing columns: {missing_columns}"
                )

            os.makedirs("artifacts", exist_ok=True)

            with open(
                self.validation_config.validation_report_path,
                "w"
            ) as f:
                for line in report:
                    f.write(line + "\n")

            logging.info("Validation Completed")

            return True

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataValidation()

    result = obj.validate_dataset(
        "artifacts/train.csv"
    )

    print("Validation Status:", result)