from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
# from sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.pipeline.training_pipeline import TrainPipeline

# def test():
#     try:
#         logging.info("Error due to divide by zero")
#         a=3/0
#     except Exception as e:
#         # raise e
#         raise SensorException(e,sys)    

if __name__ =="__main__":
    # file_path = r'C:\Users\Pramodkumar\Desktop\Project_All\ML2\sensor\aps_failure_training_set1.csv'
    # database_name="sensordb"
    # collection_name= "sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    

    # try:
    #     test()
    # except Exception as e:
    #     print(e)