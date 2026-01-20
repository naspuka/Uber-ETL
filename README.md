Overview
This project demonstrates a data engineering workflow using Airflow for orchestration, dbt for transformations, and Postgres as the destination database. Optionally, Spark can be used as a data source or intermediate processing layer.

Tech Stack


Airflow – Workflow orchestration


dbt – SQL-based transformations and modeling


Postgres – Destination database


Spark – Optional data processing engine



Getting Started
Prerequisites


Docker & Docker Compose


Python 3.10+


dbt CLI


Airflow CLI (optional, if not using Docker)


Setup


Clone the repository


git clone <repo_url>
cd <project_folder>



Start services with Docker Compose


docker-compose up -d


Make sure docker-compose.yml contains services for Postgres, Airflow, and Spark (if used).



Configure dbt




Edit profiles.yml (usually at ~/.dbt/profiles.yml):


custom_postgres:
  outputs:
    dev:
      type: postgres
      host: destination_postgres   # Replace if using another host
      user: postgres
      password: secret
      port: 5432
      dbname: destination_db
      schema: public
      threads: 1
  target: dev



Run dbt models


dbt run --profiles-dir ~/.dbt



Airflow orchestration




Access the Airflow UI at http://localhost:8080


Trigger DAGs that run dbt models or other ETL tasks.



Notes


The host for services in Docker Compose should use service names, not localhost.
Example:
host: spark-thrift  # Spark service inside Docker



Airflow DAGs can orchestrate dbt models automatically.



Optional: Spark Integration


Connect to Spark Thrift server using the host name from Docker Compose.


Use PySpark or SQL queries for intermediate transformations.



References


Airflow Docs


dbt Docs


Postgres Docs


Spark SQL



I can also make a super concise version specifically for your DE workflow that explains the orchestration flow step by step.
Do you want me to do that?