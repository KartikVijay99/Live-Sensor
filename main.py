from Sensor.Exception import SensorException
from Sensor.Logger import logging
import sys , os 

def try_Exception ( ) : 
    try : 
        logging.info("Yha error  division by error")
        a = 1 / 0
    except Exception as e :
        raise SensorException ( e , sys )

if __name__ == "__main__" :
    try : 
        try_Exception()
    except Exception as e :
        print (e )   
    


