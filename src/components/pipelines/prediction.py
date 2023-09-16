import pandas as pd
import numpy as np
from src.exception import CustomException
#from src.utils import save_object
from src.logger import logging
from src.utils  import load_object
import os
import sys

class predictpipline:
    def __init__(self):
        pass
    def predict(self):
        try:
            preprocessor_path=os.path.join("artifcats","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            data_scaled=preprocessor.transform(features)                                   
            pred=model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.info("excetion has occured")
            raise CustomException(e,sys)
class Customdata:
    def __init__(self, carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

        

    def get_data(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


