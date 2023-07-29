import logging
import pandas as pd
from datetime import datetime

class Processor:

    def __init__(self):
        self.data_count = 0
        self.latest_date = datetime(1970,1,1)
        self.msg = ""
        self.logger = logging.getLogger()

    def process(self, df, context, *args, **kwargs):
        if isinstance(df, pd.DataFrame):
            self.data_count += df.shape[0]
        elif isinstance(df, list):
            self.data_count += len(df)
        
        return df
    
    def get_msg(self):
        if self.msg == "":
            self.msg = "Processing `{}` amount of data.".format(self.data_count)

        return self.msg

    def count(self):
        return self.data_count
    
    def latest(self) -> datetime:
        return self.latest_date

    def close(self):
        pass

    def get_source(self):
        return []
    
    def get_sink(self):
        return []
