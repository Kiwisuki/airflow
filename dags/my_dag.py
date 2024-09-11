from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 10),
    'retries': 1
}

# Initialize the DAG
dag = DAG(
    'simple_dag_example',   # DAG name
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',  # Run once a day
)

# Task 1: Print start message
def print_start_message():
    print("Starting the DAG!")

start_task = PythonOperator(
    task_id='start_message',
    python_callable=print_start_message,
    dag=dag
)

# Task 2: Sleep for 5 seconds
def sleep_task():
    time.sleep(5)

sleep_task = PythonOperator(
    task_id='sleep_task',
    python_callable=sleep_task,
    dag=dag
)

# Task 3: Print completion message
def print_completion_message():
    print("DAG complete!")

completion_task = PythonOperator(
    task_id='completion_message',
    python_callable=print_completion_message,
    dag=dag
)

# Define the task dependencies
start_task >> sleep_task >> completion_task
