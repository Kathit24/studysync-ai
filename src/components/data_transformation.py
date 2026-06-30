import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join(
        "artifacts",
        "preprocessor.pkl"
    )


class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:

            numerical_columns = [
                "age",
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
            ]

            categorical_columns = [
                "gender",
                "learning_style",
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False
                        )
                    )
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns),
                ]
            )

            logging.info("Preprocessor object created successfully")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and Test datasets loaded successfully")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "final_gpa"

            input_feature_train_df = train_df.drop(
                columns=[target_column_name],
                axis=1
            )

            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(
                columns=[target_column_name],
                axis=1
            )

            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing...")

            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )

            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            train_arr = pd.concat(
                [
                    pd.DataFrame(input_feature_train_arr),
                    target_feature_train_df.reset_index(drop=True),
                ],
                axis=1,
            )

            test_arr = pd.concat(
                [
                    pd.DataFrame(input_feature_test_arr),
                    target_feature_test_df.reset_index(drop=True),
                ],
                axis=1,
            )

            save_object(
                self.data_transformation_config.preprocessor_obj_file_path,
                preprocessing_obj,
            )

            logging.info("Preprocessor saved successfully")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    print("Program Started")

    obj = DataTransformation()

    train_arr, test_arr, preprocessor_path = obj.initiate_data_transformation(
        "artifacts/train.csv",
        "artifacts/test.csv",
    )

    print("===================================")
    print("Train Shape :", train_arr.shape)
    print("Test Shape  :", test_arr.shape)
    print("Preprocessor:", preprocessor_path)
    print("===================================")