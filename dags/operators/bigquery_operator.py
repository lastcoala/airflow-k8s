from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context
from typing import Sequence

class HelloOperator(BaseOperator):

    template_fields: Sequence[str] = ("sql",)
    template_ext = ".sql"

    def __init__(self, sql, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql
    
    def execute(self, context: Context):
        print(self.sql)

