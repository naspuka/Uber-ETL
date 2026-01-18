from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bronze_tlc_ingestion",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False,
    tags=["bronze", "tlc"]
) as dag:
    download = BashOperator(
        task_id="download_tlc_data",
        bash_command="source /opt/airflow/venv/bin/activate && python scripts/download_tlc_data"
    )
    ingest = BashOperator(
        task_id="spark_bronze_ingest",
        bash_command="source /opt/airflow/venv/bin/activate && spark-submit spark/bronze_ingest_trips.py"
    )
    download >> ingest