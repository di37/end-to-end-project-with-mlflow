import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *

def objective(params, train, valid, y_val):
    with mlflow.start_run():
        # Setting up tags - developer and model
        mlflow.set_tag("model", "xgboost")
        mlflow.set_tag("developer", "isham")

        # Tracking hyperparams
        mlflow.log_params(params)
        booster = xgb.train(
            params=params,
            dtrain=train,
            num_boost_round=1000,
            evals=[(valid, 'validation')],
            early_stopping_rounds=50
        )
        y_pred = booster.predict(valid)
        rmse = mean_squared_error(y_val, y_pred, squared=False)

        # Tracking evaluation metric
        mlflow.log_metric("rmse", rmse)

    return {'loss': rmse, 'status': STATUS_OK}