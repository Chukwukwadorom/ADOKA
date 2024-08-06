from kidney_disease_classifier.config.configuration import ConfigurationManager
from kidney_disease_classifier.components.data_ingestion import DataIngestion
from kidney_disease_classifier import logger

stage_name = "Data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main (self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e