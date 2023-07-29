import logging
from typing import Sequence

from airflow.template.templater import Templater

class Source(Templater):

    def __init__(self):
        self.data_count = 0
        self.counter = 0
        self.next = True
        self.msg = ""
        self.logger = logging.getLogger()
    
    def get(self, context, *args, **kwargs):
        return None
    
    def has_next(self):
        temp = self.next
        self.next = False
        return temp
    
    def get_msg(self):
        if self.msg == "":
            self.msg = "Retrieving `{}` amount of data.".format(self.data_count)

        return self.msg

    def close(self):
        pass
    
    def count(self):
        return self.data_count

    def get_source(self):
        return []
    
    def get_sink(self):
        return []