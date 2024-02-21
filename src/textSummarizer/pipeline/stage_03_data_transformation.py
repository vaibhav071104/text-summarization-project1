
from distutils import config
from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.entity import DataTransformationConfig



class DatatransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
    data_transformation_config = config.get_data_transformation_config()
    data_transformation = DataTransformation(config=DataTransformationConfig)
    data_transformation.convert()