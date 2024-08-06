from src.kidney_disease_classifier import logger
from kidney_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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