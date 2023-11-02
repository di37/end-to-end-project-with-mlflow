import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *
from wine_quality.models import *


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def train(self):
        with mlflow.start_run():
            # Setting up tags - developer and model
            mlflow.set_tag("model", "xgboost")
            mlflow.set_tag("developer", "isham")

            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            # Tracking dataset
            mlflow.log_param("train_data", self.config.train_data_path)
            mlflow.log_param("test_data", self.config.test_data_path)

            train_x = train_data.drop([self.config.target_column], axis=1)
            test_x = test_data.drop([self.config.target_column], axis=1)
            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]

            # Model Training
            lr = ElasticNet(
                alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42
            )
            lr.fit(train_x, train_y)

            # Predictions
            y_pred = lr.predict(test_x)

            # Model Evaluation
            (rmse, mae, r2) = self.eval_metrics(test_y, y_pred)

            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Tracking parameters and evaluation metric
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Saving the model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(lr, model_path)

            # Saving the model in AWS and Registering model
            # mlflow.log_artifact(local_path=model_path, artifact_path="models_pickle")
            mlflow.sklearn.log_model(
                lr, "model", registered_model_name="ElasticnetModel"
            )
