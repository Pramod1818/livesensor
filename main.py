from sensor.exception import SensorException
import os,sys
from sensor.logger import logging

def test():
    try:
        logging.info("Error due to divide by zero")
        a=3/0
    except Exception as e:
        # raise e
        raise SensorException(e,sys)    

if __name__ =="__main__":
    try:
        test()
    except Exception as e:
        print(e)