FROM apache/airflow:latest-python3.11

USER root

# Install Docker CLI
RUN apt-get update && apt-get install -y \
    docker.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Install Apache Airflow Docker Provider
RUN pip install --no-cache-dir apache-airflow-providers-docker