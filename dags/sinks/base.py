import logging

class Sink:
    def __init__(self):
        self.data_count = 0
        self.msg = ""
        self.logger = logging.getLogger()

    def put(self, df, context, *args, **kwargs):
        pass
    
    def close(self):
        pass

    def get_msg(self):
        if self.msg == "":
            self.msg = "Ingesting `{}` amount of data.".format(self.data_count)

        return self.msg
        
    def count(self):
        return self.data_count
    
    def get_sink(self):
        return []