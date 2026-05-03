import pandas as pd
import pandera.pandas as pa
from pandera import Check
from pathlib import Path

current_dir = Path.cwd()
path_to_data = current_dir.parent / 'data' / 'sleep_dataset.csv'

df = pd.read_csv(path_to_data)

def data_preparation():
    df['date'] = pd.to_datetime(df['date'])
    df['bedtime'] = pd.to_datetime(df['bedtime'], format='%H:%M')
    df['wake_time'] = pd.to_datetime(df['wake_time'], format='%H:%M')

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


print(df)






