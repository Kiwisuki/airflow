from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

host = 'host.docker.internal'

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'docker_operator_example',
    default_args=default_args,
    description='An example DAG with DockerOperator',
    schedule_interval=None,
)

# Define the DockerOperator task
run_docker_task = DockerOperator(
    task_id='run_docker_container',
    image='kiwisaki/redp:scraping-service-latest',  # Replace with your image
    network_mode='bridge',  # Optional: specify if using network mode
    docker_url='unix://var/run/docker.sock',
    api_version='auto',
    auto_remove=True,  # Auto-remove container after running
    mount_tmp_dir=False,  # Mount tmp dir
    dag=dag,
)

