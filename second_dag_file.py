from airflow import DAG

from datetime import timedelta, datetime

from airflow.operators.python_operator import PythonOperator

import os
import boto3
import awswrangler as wr
import pandas as pd
import requests


from dotenv import load_dotenv

load_dotenv()

"""
defining the function to fetch the data from the endpoint
and save the result in a dataframe
"""

def results_df():

    url = 'https://randomuser.me/api/?results=10'
    response = requests.get(url)

    if response.status_code == 200:
        response_url = response.json()
        results = response_url["results"]
        
    else:
        print("Error: Unable to fetch data from the API")

    results_df = pd.DataFrame(results)

    return results_df



"""
This function defines the parameters for the aws_session connection
"""
def aws_session():
    session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key'),
    aws_secret_access_key=os.getenv('aws_secret_key'),
    region_name=os.getenv('region'))
    return session

"""
defining the function to export the results in the dataframe
into the defined bucket path in aws
"""

def upload_to_aws():
    wr.s3.to_csv(
    df=results_df(),
    path="s3://toludebuckets/random_users_api/results",
    boto3_session=aws_session(),
    mode="append",
    dataset=True
    )
    return



#defining my default arguments
default_args = {
        'owner' : 'airflow',
        'start_date' : datetime(2022, 11, 12)
}

#defining my DAG parameters
dag = DAG(
    dag_id = "tolu_dag2",
    description='my_first_dag',
    default_args=default_args,
    catchup=False
)


#defining my task parameter using Python Operator
task1 = PythonOperator(
    python_callable = upload_to_aws,
    dag=dag,
    task_id = 'task1'
)

task1