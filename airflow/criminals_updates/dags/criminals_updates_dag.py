from airflow import DAG
from airflow.models import Variable
import datetime
from criminals_updates_operator import CriminalsUpdatesOperatop



default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='criminal_updates_dag',
    default_args=default_args,
    schedule_interval='20 12,20 * * *',
    start_date=datetime.datetime(2022, 5, 1),
    tags=['Criminals', 'Updates'],
) as dag:

    CriminalsUpdatesOperatop(
        task_id ='criminals_updates',
        sender = 'kvtimm@gmail.com',
        password = Variable.get('password'),
        recipients = ['kvtimm@gmail.com', 'alexbirallex@gmail.com']
    )
