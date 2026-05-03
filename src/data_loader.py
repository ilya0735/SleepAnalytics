import pandas as pd
import pandera.pandas as pa
from pandera import Check
from pathlib import Path
from utils import *

@timer
@logger
def data_loader():
    base = Path(__file__).resolve().parent.parent
    path_to_data = base / 'data' / 'sleep_dataset.csv'

    dataset = pd.read_csv(path_to_data)
    return dataset

df = data_loader()

@timer
@logger
def data_preparation():
    df['date'] = pd.to_datetime(df['date'])
    df['bedtime'] = pd.to_datetime(df['bedtime'], format='%H:%M')
    df['wake_time'] = pd.to_datetime(df['wake_time'], format='%H:%M')

@timer
@logger
def validate_df():
    schema = pa.DataFrameSchema({
        'date': pa.Column(str),
        'day_of_week': pa.Column(str),
        'bedtime': pa.Column(str),
        'wake_time': pa.Column(str),
        'total_sleep_hours': pa.Column(float, checks=Check.in_range(0, 25)),
        'deep_sleep_hours': pa.Column(float, checks=Check.in_range(0, 25)),
        'rem_sleep_hours': pa.Column(float, checks=Check.in_range(0, 25)),
        'awakenings': pa.Column(int),
        'sleep_quality': pa.Column(str, checks=Check.isin(['excellent', 'good', 'average', 'poor', 'very_poor'])),
    })
    return schema.validate(df)

@timer
@logger
def post_preparation_validate():
    schema = pa.DataFrameSchema({
        'date': pa.Column(pa.DateTime),
        'bedtime': pa.Column(pa.DateTime),
        'wake_time': pa.Column(pa.DateTime),
    })
    return schema.validate(df)


try:
    validate_df()
    data_preparation()
    post_preparation_validate()
except Exception as e:
    print("Нарушена структура данных", e)









