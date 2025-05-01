from airflow import DAG

from datetime import timedelta, datetime

from airflow.operators.python_operator import PythonOperator

from upload_to_aws import upload_to_aws


#defining my default arguments
default_args = {
        'owner' : 'airflow',
        'start_date' : datetime(2022, 11, 12),

}

#defining my DAG parameters
dag = DAG(
    dag_id = "tolu_dag21",
    description='my_first_dag',
    default_args=default_args,
    catchup=False
)

task1 = PythonOperator(
    python_callable = upload_to_aws,
    dag=dag,
    execution_timeout=timedelta(seconds=180),
    task_id = 'task1'
)

task1
