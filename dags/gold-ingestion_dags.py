from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 1, 18),
    "retries": 1,
}

with DAG(
    dag_id="silver_to_gold_dbt",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    silver_to_gold = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd /opt/airflow/dags && dbt run --profiles-dir /opt/airflow/.dbt"
    )

    test_gold = BashOperator(
        task_id="run_dbt_tests",
        bash_command="cd /opt/airflow/dags && dbt test --profiles-dir /opt/airflow/.dbt"
    )
    silver_to_gold >> test_gold
