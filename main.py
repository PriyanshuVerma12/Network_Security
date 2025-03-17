import sys
from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_transformation import DataTransformation
from network_security.components.data_validation import DataValidation
from network_security.components.model_trainer import ModelTrainer
from network_security.entity.artifact_entity import DataIngestionArtifact
from network_security.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainerConfig, TrainingPipelineConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.logging import logger

try:
    logger.logging.info("Data Ingestion Initiated")
    training_pipeline_config=TrainingPipelineConfig()
    data_ingestion_config=DataIngestionConfig(training_pipeline_config)
    obj = DataIngestion(data_ingestion_config)
    data_Ingestion_Artifact= obj.initiate_data_ingestion()
    # print(data_Ingestion_Artifact)
    logger.logging.info("Data Ingestion Completed")

    logger.logging.info("Data Validation Initiated")
    data_validation_config=DataValidationConfig(training_pipeline_config)
    obj = DataValidation(data_Ingestion_Artifact,data_validation_config)
    data_Validation_Artifact= obj.initiate_data_validation()
    # print(data_Validation_Artifact)
    logger.logging.info("Data Validation Completed")

    logger.logging.info("Data Transformation Initiated")
    data_transformation_config=DataTransformationConfig(training_pipeline_config)
    obj=DataTransformation(data_Validation_Artifact,data_transformation_config)
    data_transformation_artifact = obj.initiate_data_transformation()
    # print(data_transformation_artifact)
    logger.logging.info("Data Transformation Completed")

    logger.logging.info("Model Training and Evaluation Initiated")
    model_trainer_config=ModelTrainerConfig(training_pipeline_config)
    obj = ModelTrainer(model_trainer_config,data_transformation_artifact)
    model_trainer_artifact = obj.initiate_model_trainer()
    # print(model_trainer_artifact)
    logger.logging.info("Model Training and Evaluation Completed")

except Exception as e:
        raise NetworkSecurityException(e,sys)

