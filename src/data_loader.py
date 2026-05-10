from datetime import timedelta
import pandas as pd
import pandera.pandas as pa
from pandera import Check
from pathlib import Path
from src.utils import *


class DataLoader:
    def __init__(self):
        self.__df = pd.DataFrame(self.__data_loader())
        self.__full_check()

    @timer
    @logger
    def __data_loader(self):
        base = Path(__file__).resolve().parent.parent
        path_to_data = base / 'data' / 'night_owl_final_distorted.csv'

        dataset = pd.read_csv(path_to_data)
        return dataset

    @staticmethod
    def __normalize(bedtime):
        if bedtime.hour < 16:
            return timedelta(hours=bedtime.hour, minutes=bedtime.minute)
        else:
            return timedelta(days=-1, hours=bedtime.hour, minutes=bedtime.minute)

    @timer
    @logger
    def __data_formating(self):
        self.__df['date'] = pd.to_datetime(self.__df['date'])
        self.__df['bedtime'] = pd.to_datetime(self.__df['bedtime'], format='%H:%M')
        self.__df['wake_time'] = pd.to_datetime(self.__df['wake_time'], format='%H:%M')
        self.__df['bedtime'] = self.__df['bedtime'].apply(self.__normalize)
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.__df['day_of_week'] = pd.Categorical(self.__df['day_of_week'], categories=day_order, ordered=True)
        quality_order = ['very_poor', 'poor', 'average', 'good', 'excellent']
        self.__df['sleep_quality'] = pd.Categorical(self.__df['sleep_quality'], categories=quality_order, ordered=True)

    @timer
    @logger
    def __validate_df(self):
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
        return schema.validate(self.__df)

    @timer
    @logger
    def __post_preparation_validate(self):
        schema = pa.DataFrameSchema({
            'date': pa.Column(pa.DateTime),
            'bedtime': pa.Column(pa.Timedelta),
            'wake_time': pa.Column(pa.DateTime),
        })
        return schema.validate(self.__df)

    @logger
    def __full_check(self):
        try:
            self.__validate_df()
            self.__data_formating()
            self.__post_preparation_validate()
        except Exception as e:
            print("Нарушена структура данных", e)

    @property
    def df(self):
        return self.__df

DL = DataLoader()
df = DL.df