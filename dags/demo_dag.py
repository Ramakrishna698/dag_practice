# dags/dag_gcs_to_bq.py

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    dag_id="demo_auto_deploy",
    start_date=datetime(2024,1,1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    start >> end