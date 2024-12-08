# ETL Project with Data Fusion, Airflow, and BigQuery

This repository contains the code and configuration files for an Extract, Transform, Load (ETL) pipeline project combined with predictive analytics capabilities. It leverages Google Cloud Data Fusion for data transformation, Apache Airflow (via Cloud Composer) for orchestration, Google BigQuery for data storage, and BigQuery ML for predictive modeling.

## Overview

The project aims to perform the following tasks:

1. **Data Extraction**: Extract data using python.
2. **Data Masking**: Apply data masking & encoding techniques to sensitive information in Cloud Data Fusion before loading it into BigQuery.
3. **Data Loading**: Load transformed data into Google BigQuery tables.
4. **Using BigQuery ML**: Predictive models are trained to forecast employee salaries based on roles, departments, and other features.
5. **Orchestration**: Automate complete Data pipeline using Airflow ( Cloud Composer )

![image](https://github.com/vishal-bulbule/etl-pipeline-datafusion-airflow/assets/143475073/755818fe-1cd3-4e1c-827d-35b963d6f414)

## Architecture

![image](https://github.com/vishal-bulbule/etl-pipeline-datafusion-airflow/assets/143475073/0ea51bdb-99cc-4abf-8ccc-8be721462fc3)
