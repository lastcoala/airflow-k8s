from airflow.models import BaseOperator

from processors.base import Processor
from sinks.base import Sink
from sources.base import Source

import traceback

class GenericOperator(BaseOperator):
    def __init__(
        self,
        source: Source=Source(),
        sink: Sink=Sink(),
        processor: Processor=Processor(),
        *args,
        **kwargs
    ):
        super(GenericOperator, self).__init__(*args, **kwargs)
        self.source = source
        self.sink = sink
        self.processor = processor

    def execute(self, context):
        iteration = 0
        msg = ""
        status = "success"

        data_count = 0
        tmp_context = {"iteration": iteration, "generic_operator": self, "error": None}
        new_ctx = {**context, **tmp_context}

        try:
            data_count_total = 0
            while self.source.has_next():
                self.log.info("Retrieving data")
                input = self.source.get(new_ctx)

                self.log.info("Processing data")
                processed = self.processor.process(input, new_ctx)
                
                data_count_total += self.processor.count()

                self.log.info("Outputting data")
                self.sink.put(processed, new_ctx)

                new_ctx["iteration"] += 1

            msg = self.source.get_msg() + " " + self.processor.get_msg() + " " + self.sink.get_msg()

            data_count = self.processor.count()
            if data_count == 0:
                data_count = self.sink.count()
            if data_count == 0:
                data_count = self.source.count()

            self.log.info(msg)

        except Exception as e:
            msg = traceback.format_exc()
            data_count = 0
            status = None
            new_ctx["error"] = e
            self.log.error(msg)

        finally:
            self.sink.close()
            self.processor.close()
            self.source.close()
        
        if status is None:
            raise ValueError(msg)
