import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime as dt

log = logging.getLogger(__name__)

args = {
    'owner': 'admin',
    'start_date': dt.datetime(2022, 4, 23),
    'depends_on_past': False
}


def get_exchange_rates():
    print('Parsing sites with exchange rates')


def get_user_location():
    print('Parsing sites with exchange rates')


def get_amount_to_exchange():
    print('Receiving from the user the amount that he wants to exchange')


def get_exchangers_location():
    print('Getting the locations of exchangers (parsing some maps or bank websites with this data)')


def get_transport_cost():
    print('Getting the price of petrol / public transport (parsing sites with this data)')


def get_route_to_exchangers():
    print('Map parsing, where you can build routes by car / public transport / taxi (Yandex maps for example)')


def get_route_cost_to_exchangers():
    print('Calculation of the fare for all types of transport to all exchangers')


def get_the_best_exchanger_by_car():
    print('Calculation of the most profitable exchanger if you go by car')


def get_the_best_exchanger_by_taxi():
    print('Calculation of the most profitable exchanger if you go by taxi')


def get_the_best_exchanger_by_public_transport():
    print('Calculation of the most profitable exchanger if you go by public transport')


with DAG('the_most_profitable_exchanger', default_args=args, schedule_interval=None, catchup=False) as dag:

    get_exchange_rates = PythonOperator(
        task_id='exchange_rates',
        python_callable=get_exchange_rates,
        dag=dag
    )

    get_user_location = PythonOperator(
        task_id='user_location',
        python_callable=get_user_location,
        dag=dag
    )

    get_amount_to_exchange = PythonOperator(
        task_id='amount_to_exchange',
        python_callable=get_amount_to_exchange,
        dag=dag
    )

    get_exchangers_location = PythonOperator(
        task_id='exchangers_location',
        python_callable=get_exchangers_location,
        dag=dag
    )

    get_transport_cost = PythonOperator(
        task_id='transport_cost',
        python_callable=get_transport_cost,
        dag=dag
    )

    get_route_to_exchangers = PythonOperator(
        task_id='route_to_exchangers',
        python_callable=get_route_to_exchangers,
        dag=dag
    )

    get_route_cost_to_exchangers = PythonOperator(
        task_id='route_cost_to_exchangers',
        python_callable=get_route_cost_to_exchangers,
        dag=dag
    )

    get_the_best_exchanger_by_car = PythonOperator(
        task_id='the_best_exchanger_by_car',
        python_callable=get_the_best_exchanger_by_car,
        dag=dag
    )

    get_the_best_exchanger_by_taxi = PythonOperator(
        task_id='the_best_exchanger_by_taxi',
        python_callable=get_the_best_exchanger_by_taxi,
        dag=dag
    )

    get_the_best_exchanger_by_public_transport = PythonOperator(
        task_id='the_best_exchanger_by_public_transport',
        python_callable=get_the_best_exchanger_by_public_transport,
        dag=dag
    )

    get_user_location >> get_route_to_exchangers
    get_exchangers_location >> get_route_to_exchangers
    get_route_to_exchangers >> get_route_cost_to_exchangers
    get_transport_cost >> get_route_cost_to_exchangers
    get_route_cost_to_exchangers >> get_the_best_exchanger_by_car
    get_route_cost_to_exchangers >> get_the_best_exchanger_by_taxi
    get_route_cost_to_exchangers >> get_the_best_exchanger_by_public_transport
    get_exchange_rates >> get_the_best_exchanger_by_car
    get_exchange_rates >> get_the_best_exchanger_by_taxi
    get_exchange_rates >> get_the_best_exchanger_by_public_transport
    get_amount_to_exchange >> get_the_best_exchanger_by_car
    get_amount_to_exchange >> get_the_best_exchanger_by_taxi
    get_amount_to_exchange >> get_the_best_exchanger_by_public_transport
