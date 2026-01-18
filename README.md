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


🚀 Phase 1: Bronze Layer — Code Development (Apple Silicon)
What We Are Building (ONLY Bronze)

Goal
Ingest raw TLC Uber/Taxi trip data → store immutable raw data in MinIO (S3-compatible) → register ingestion via Airflow.

NO transformations yet
NO dbt yet
NO analytics yet

This matches real-world medallion architecture.

Option A: Fully Dockerized Spark + Python

❌ On Apple Silicon:

Slow

JVM crashes

Hadoop native libs pain

Volume permission issues

Harder debugging

Option B: Hybrid (What We’re Doing)

✅ What runs in Docker:

Stateful services (DB, object storage, scheduler)

✅ What runs locally:

Spark

Python ETL logic

This gives:

Faster iteration

Better debugging

Lower memory overhead

Cleaner stack for a Mac Air

4️⃣ Why Airflow Is in Docker but Code Isn’t (Yet)

Right now Airflow:

Orchestrates

Triggers commands

Does not execute heavy Spark workloads itself

Later we will move execution into containers (Kubernetes-style thinking), but:

You do NOT start with that complexity

This mirrors:

Local dev → staging → production

EMR / Dataproc / K8s job execution

5️⃣ This Matches Real Enterprise Patterns

Here’s how this looks in real life:

Layer	Where it runs
Airflow	K8s / Docker
Spark jobs	EMR / Dataproc / Yarn
Object storage	S3 / GCS
Local dev	Laptop

Your setup is a local analog of this.

6️⃣ When We WILL Dockerize the Code

Later phases:

dbt → containerized

Spark → submitted via Airflow operators

CI/CD → Docker images

But not on day one.

Trying to do that early is how projects die.

7️⃣ Portfolio Explanation (This Matters for Interviews)

If asked:

“Why didn’t you run Spark inside Docker locally?”

Your answer:

“For local development on Apple Silicon, I separated stateful services into Docker and ran Spark natively to avoid JVM and Hadoop native library issues. In production this would map to Airflow orchestrating Spark jobs on managed compute like Dataproc or EMR.”

That answer wins interviews.

8️⃣ Summary (Burn This In)

Docker runs services

Python needs client SDKs

Spark is better native on Apple Silicon

This is intentional architecture, not a shortcut

You are building this the right way

CSV

❌ Spark reads every row, then filters

Parquet

✅ Spark:

Reads only fare and pickup_date

Skips entire row groups using metadata

This is why Parquet is data-lake gold standard.

6️⃣ Compression Without Pain
Format	Compression
CSV	gzip (whole file)
Parquet	Snappy/ZSTD (per column)

7️⃣ Evolution & Compatibility
Feature	CSV	Parquet
Add columns	Breaks consumers	Safe
Rename columns	Manual fixes	Managed
Partition aware	❌ No	✅ Yes
Schema evolution	❌	✅


✅ What You Have Achieved

You now have:

Proper Bronze layer

Raw immutable data

Spark ingestion

S3-compatible object storage

Airflow orchestration

Apple Silicon–safe stack

we move to:
➡️ Silver layer transformations (PySpark + data quality)
➡️ Then dbt
➡️ Then Gold analytics models


Silver Layer – What It Does (Precisely)

Input:

Bronze Parquet (raw, minimally processed)

Output:

Clean, typed, trusted Parquet

Partitioned for analytics

Ready for dbt

Silver responsibilities (non-negotiable):

Schema enforcement (NO inference)

Data type normalization

Null & range validation

Business feature derivation

Standard column naming

Reject / filter bad records

Silver is where “data engineering” actually happens.

2️⃣ Silver Data Quality Rules (Explicit)

Assume Uber/TLC-like data.

Hard Rules (Rows failing these are dropped)

pickup_datetime IS NOT NULL

dropoff_datetime IS NOT NULL

trip_distance > 0

fare_amount >= 0

dropoff_datetime >= pickup_datetime

Soft Rules (Clean / standardize)

Cast timestamps to UTC

Cast numeric fields explicitly

Normalize column names to snake_case

Derived Fields (Silver-only)

trip_duration_minutes

pickup_date

pickup_hour

time_of_day (morning/afternoon/evening/night)

4️⃣ Why This Is Correct (Important)
✅ Why explicit schema?

Prevents silent type corruption

Makes failures loud

Interview gold

✅ Why partition by pickup_date?

Most queries filter by date

Enables predicate pushdown

Reduces scan cost

✅ Why Spark (not dbt) here?

Row-level logic

Heavy computation

Data quality enforcement

1️⃣ What dbt will do in your architecture

Input: Silver Parquet data in MinIO

Engine: Spark (via dbt-spark)

Output: Gold analytics tables (facts & dimensions)

Role: SQL transformations, tests, docs — not ingestion

2️⃣ Create dbt project (locally, not in Airflow yet)


What you should see now

Inside Spark (not MinIO):

A managed Spark table:

gold.gold_trip_metrics


Queryable via:

dbt

Spark SQL

Thrift clients (Beeline, DBeaver, etc.)

You can confirm via Spark UI:

http://localhost:18080

Why this is portfolio-ready 🔥

You now have:

Bronze → raw parquet (MinIO)

Silver → cleaned, partitioned parquet

Gold → analytics tables via dbt + Spark

Airflow-ready orchestration

Cloud-style object storage

Zero paid tools

Apple Silicon compatible

This is real data engineering, not a toy project.


✅ What you’ve proven
1️⃣ dbt → Spark Thrift is working

dbt created gold.gold_trip_metrics

Spark registered it in the metastore

Thrift server exposed it

Beeline queried it successfully

This is exactly how enterprises run dbt on Spark.

2️⃣ Medallion architecture is complete
Layer	Technology	Verified
Bronze	Raw Parquet in MinIO	✅
Silver	Cleaned + partitioned Parquet	✅
Gold	dbt → Spark SQL tables	✅
Query	Thrift / JDBC	✅

Your query output is aggregated analytics, not raw data — that’s the Gold layer done right.

3️⃣ Numbers make sense (important)

Trips grouped by pickup_date + time_of_day

Metrics are realistic

No null explosions

Aggregations are stable

This shows your Silver data quality logic worked.

🚀 Portfolio value (this is what matters)

If someone asks:

“Have you ever built a lakehouse?”

You can now say yes and show:

Dockerized infra

Object storage (MinIO)

Spark ETL (Bronze → Silver)

dbt transformations (Silver → Gold)

Spark Thrift + JDBC querying

Apple Silicon compatible setup

That puts you ahead of most applicants.

schema.yml
✅ What you’ve achieved (important)

Fixed metric correctness (real-world validation)

Added data quality enforcement

Gold layer is now trustworthy + production-grade

This is exactly what interviewers look for.
2️⃣ Make Gold incremental
