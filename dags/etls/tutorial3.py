from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from utils.time import date_jkt
from utils.path import path

from operators.bigquery_operator import HelloOperator

with DAG(
    "tutorial3",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule="7 1 * * *",
    start_date=date_jkt(2023,7,23),
    catchup=True,
    tags=["example"],
) as dag:

    t1 = HelloOperator(
        task_id="print_date",
        sql=path("etls/templates/user.sql "),
    )