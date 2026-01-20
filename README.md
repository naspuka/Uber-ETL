# Uber Data Analytics Dashboard (Open-Source Data Engineering Project)

## 📌 Project Overview
This project is an **end-to-end open-source data engineering pipeline** designed to analyze Uber ride data and produce analytics-ready datasets and dashboards. The goal is to simulate a **real-world production-grade data platform** using only **open-source tools**, covering data ingestion, transformation, orchestration, and visualization.

You will build this project **start to finish**, focusing on best practices used by data engineers in industry.

---

## 🎯 Objectives
- Build a complete **ETL/ELT pipeline** using open-source technologies
- Apply **data modeling and analytics engineering** principles
- Orchestrate workflows using **Apache Airflow**
- Transform data using **dbt**
- Store and query analytical data efficiently
- Create an interactive **analytics dashboard**
- Document and structure the project like a real production repository

---

## 🧱 Architecture Overview

**High-level flow:**

```
Raw Data (CSV / Parquet)
        ↓
Data Ingestion (Python)
        ↓
Raw Storage (PostgreSQL / Data Lake)
        ↓
Transformations (dbt)
        ↓
Analytics Layer (Star Schema)
        ↓
Visualization (Superset / Metabase)
```

**Orchestration:** Apache Airflow controls ingestion, transformation, and validation workflows.

---

## 🛠️ Technology Stack (100% Open Source)

| Layer | Tool |
|-----|-----|
| Ingestion | Python (Pandas, PyArrow) |
| Orchestration | Apache Airflow |
| Storage | PostgreSQL (or DuckDB for local) |
| Transformation | dbt Core |
| Data Modeling | Star Schema |
| Visualization | Apache Superset / Metabase |
| Version Control | Git + GitHub |
| Containerization (Optional) | Docker |

---

## 📂 Dataset

### Source Options
- Public Uber / NYC Taxi datasets
- Kaggle ride-hailing datasets
- Synthetic Uber-like data generated using Python

### Example Raw Fields
- `ride_id`
- `pickup_datetime`
- `dropoff_datetime`
- `pickup_location`
- `dropoff_location`
- `trip_distance`
- `fare_amount`
- `payment_type`
- `driver_id`

---

## 🗃️ Data Modeling

### Analytics Schema (Star Schema)

#### Fact Table
- `fact_trips`
  - trip_id
  - pickup_time_id
  - dropoff_time_id
  - pickup_location_id
  - dropoff_location_id
  - driver_id
  - fare_amount
  - trip_distance

#### Dimension Tables
- `dim_time`
- `dim_location`
- `dim_driver`
- `dim_payment`

All transformations are handled using **dbt models**.

---

## 🔄 Data Pipeline Stages

### 1️⃣ Ingestion Layer
- Python scripts ingest raw CSV/Parquet data
- Load into PostgreSQL raw schema
- Validate schema and null values

### 2️⃣ Transformation Layer (dbt)
- Clean raw data
- Apply type casting and standardization
- Build staging models
- Create fact and dimension tables

### 3️⃣ Orchestration (Airflow)
- DAG schedules ingestion
- Triggers dbt runs
- Handles retries and logging
- Optional data quality checks

---

## 📊 Analytics & Dashboards

### Example Metrics
- Total trips per day/week/month
- Revenue trends
- Average trip distance
- Peak pickup hours
- Popular pickup/dropoff locations

### Visualization Tools
- Apache Superset (recommended)
- Metabase (simpler setup)

---

## 🧪 Data Quality Checks
- Row count validation
- Null checks on primary keys
- Accepted value checks (payment type, distance > 0)
- dbt tests

---

## 🗂️ Project Structure

```
uber-data-analytics/
│
├── airflow/
│   ├── dags/
│   └── plugins/
│
├── dbt/
│   ├── models/
│   ├── tests/
│   └── macros/
│
├── ingestion/
│   ├── ingest_data.py
│   └── utils.py
│
├── data/
│   └── raw/
│
├── dashboards/
│   └── screenshots/
│
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run (High Level)

1. Clone repository
2. Set up virtual environment
3. Start PostgreSQL
4. Load raw data
5. Run Airflow DAGs
6. Execute dbt models
7. Launch Superset dashboard

---

## 📈 Learning Outcomes

By completing this project, you will demonstrate:
- End-to-end data engineering skills
- Strong understanding of ELT pipelines
- Real-world orchestration patterns
- Analytics engineering with dbt
- Data modeling for BI

---

## 🔮 Future Enhancements
- Incremental dbt models
- Slowly Changing Dimensions (SCD)
- Streaming ingestion (Kafka)
- Data lake with Iceberg or Delta
- CI/CD for dbt and Airflow

---

## 📄 License
This project is open-source and free to use for learning and portfolio purposes.

