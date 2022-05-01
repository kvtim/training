from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from criminals_updates_operator import CriminalsUpdatesOperatop



default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='criminal_updates_dag',
    default_args=default_args,
    schedule_interval='0 12,20 * * *',
    start_date=days_ago(1),
    tags=['Criminals', 'Updates'],
) as dag:

    CriminalsUpdatesOperatop(
        task_id ='criminals_updates',
        sender = 'kvtimm@gmail.com',
        password = Variable.get('password'),
        recipients = ['temshidze777@mail.ru']
    )