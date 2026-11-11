from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.insert(0,'../')
from sklearn.ensemble import RandomForestClassifier
from src.data.loading import load_data
from src.data.cleaning import clean_data
from src.models.training_best_model import training_best_model
from src.models.evaluation import evaluation


def param_grid():
    return {
        "model__n_estimators": [200, 300, 500, 700],
        "model__max_depth": [None, 10, 20, 30],
        "model__min_samples_split": [2, 5, 10],
        "model__min_samples_leaf": [1, 2, 4, 6],
        "model__max_features": ["sqrt", "log2"],
        "model__class_weight": [None, "balanced", "balanced_subsample"]
    }
with DAG(
    dag_id="mindora_ai",
    start_date= datetime(2026,11,11),
    schedule="@daily",
    catchup=False
) as dag :
    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )
    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
        op_args=[load_data()]
    ),
    task_train = PythonOperator(
        task_id="train_model",
        python_callable=training_best_model,
        op_args=[RandomForestClassifier() , param_grid() , load_data()]
    ),
    evaluate_task = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluation,
        op_args=list(task_train)
    )
