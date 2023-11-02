import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from wine_quality import *
from utils import *

if __name__ == '__main__':
    ## Testing for Data Ingestion Pipeline
    # try:
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #     obj = DataIngestionTrainingPipeline()
    #     obj.main()
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<x==========x")
    # except Exception as e:
    #     customlogger.exception(e)
    #     raise e
    
    ## Testing for Data Validation Pipeline
    # try:
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #     obj = DataValidationTrainingPipeline()
    #     obj.main()
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<x==========x")
    # except Exception as e:
    #     customlogger.exception(e)
    #     raise e
    
    ## Testing for Data Transformation Pipeline
    # try:
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #     obj = DataTransformationTrainingPipeline()
    #     obj.main()
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #     customlogger.exception(e)
    #     raise e

    ## Testing for Model Trainer Pipeline
    # try:
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #     obj = ModelTrainerTrainingPipeline()
    #     obj.main()
    #     customlogger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #     customlogger.exception(e)
    #     raise e
