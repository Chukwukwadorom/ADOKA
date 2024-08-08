from src.kidney_disease_classifier import logger
from kidney_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidney_disease_classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
stage_name = "Data ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    stage_name  = "Prepare base model"
    try: 
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {stage_name } started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {stage_name } completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e




    stage_name = "Training"
    try: 
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e