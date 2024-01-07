##############################################################################
# Import necessary modules
##############################################################################
import importlib.util

from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import importlib.util
from datetime import datetime, timedelta


# from utils import *
# from data_validation_checks import *


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


utils = module_from_file("utils", "/home/dags/lead_scoring_data_pipeline/utils.py")

###############################################################################
# Define default arguments and DAG
###############################################################################

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

ML_data_cleaning_dag = DAG(
    dag_id='Lead_Scoring_Data_Engineering_Pipeline',
    default_args=default_args,
    description='DAG to run data pipeline for lead scoring',
    schedule_interval='@daily',
    catchup=False
)

###############################################################################
# Create a task for build_dbs() function with task_id 'building_db'
###############################################################################
building_db_task = PythonOperator(
    task_id='building_db',
    python_callable=utils.build_dbs,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for raw_data_schema_check() function with task_id 'checking_raw_data_schema'
###############################################################################
checking_raw_data_schema_task = PythonOperator(
    task_id='checking_raw_data_schema',
    python_callable=utils.raw_data_schema_check,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for load_data_into_db() function with task_id 'loading_data'
##############################################################################
loading_data_task = PythonOperator(
    task_id='loading_data',
    python_callable=utils.load_data_into_db,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for map_city_tier() function with task_id 'mapping_city_tier'
###############################################################################
mapping_city_tier_task = PythonOperator(
    task_id='mapping_city_tier',
    python_callable=utils.map_city_tier,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for map_categorical_vars() function with task_id 'mapping_categorical_vars'
###############################################################################
mapping_categorical_vars_task = PythonOperator(
    task_id='mapping_categorical_vars',
    python_callable=utils.map_categorical_vars,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for interactions_mapping() function with task_id 'mapping_interactions'
###############################################################################
mapping_interactions_task = PythonOperator(
    task_id='mapping_interactions',
    python_callable=utils.interactions_mapping,
    dag=ML_data_cleaning_dag)

###############################################################################
# Create a task for model_input_schema_check() function with task_id 'checking_model_inputs_schema'
###############################################################################
checking_model_inputs_schema_task = PythonOperator(
    task_id='checking_model_inputs_schema',
    python_callable=utils.model_input_schema_check,
    dag=ML_data_cleaning_dag)

###############################################################################
# Define the relation between the tasks
###############################################################################
building_db_task.set_downstream(checking_raw_data_schema_task)
checking_raw_data_schema_task.set_downstream(loading_data_task)
loading_data_task.set_downstream(mapping_city_tier_task)
mapping_city_tier_task.set_downstream(mapping_categorical_vars_task)
mapping_categorical_vars_task.set_downstream(mapping_interactions_task)
mapping_interactions_task.set_downstream(checking_model_inputs_schema_task)
