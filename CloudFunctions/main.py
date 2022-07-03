import requests
import sys


def main(dict):
    currency = requests.get(f'https://www.nbrb.by/api/exrates/rates/{dict["currency"]}?parammode=2 ') \
        .json()['Cur_OfficialRate']
    return {dict['currency']: f'{currency}'}
