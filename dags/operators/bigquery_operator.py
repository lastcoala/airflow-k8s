from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context
from typing import Sequence

class HelloOperator(BaseOperator):

    template_fields: Sequence[str] = ("sql", "config",)
    template_fields_renderers = {"config": "json"}
    template_ext = ".sql"

    def __init__(self, sql, config, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.config = config
    
    def execute(self, context: Context):
        print(self.sql)
        print(self.config)

