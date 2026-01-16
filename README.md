Build an Uber Data Analytics Dashboard 

This data engineering project idea revolves around analyzing Uber ride data to visualize trends and generate actionable insights. This project builds a comprehensive ETL and analytics pipeline, from ingestion to visualization, using Google Cloud Platform. 

Project Idea: Start data engineering pipeline by sourcing publicly available or simulated Uber trip datasets, for example, the TLC Trip record dataset.

Use Python and PySpark for data ingestion, cleaning, and transformation. Key operations include handling missing data, converting timestamps, and categorizing rides by parameters like time of day, trip duration, and location clusters. Store the data in in Google Cloud Storage to ensure scalability and reliability. 

For data transformation, deploy Mage on a Compute Engine VM, where it performs ETL processes like cleaning, aggregating, and enriching data. 
Store the transformed data in BigQuery, Google’s serverless data warehouse to enable high-performance analytics. 

Finally, you can deliver visualizations and insights through Looker, which integrates seamlessly with BigQuery to create interactive dashboards. This architecture showcases a modern, end-to-end cloud analytics workflow.

Phase 0: Project Bootstrap (Code Foundation)

Goal: Get a stable, reproducible local platform running before writing any data logic.

Next Step (Phase 1)

Once you confirm:

Docker is running

Airflow UI loads

MinIO UI loads

We will next:

Design Bronze ingestion contracts

Write the first ingestion script

Create the first Airflow DAG

👉 Reply with “Infra is up” (or paste errors if not).