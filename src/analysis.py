from datetime import datetime

import numpy as np

from src.data_loader import df
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def month_generator(month):
    for i, ROW in df.iterrows():
        if ROW['date'].month == month:
            yield ROW

def day_of_week_generator(day):
    for i, ROW in df.iterrows():
        if ROW['day_of_week'] == day:
            yield ROW

def sleep_quality_generator(quality):
    for i, ROW in df.iterrows():
        if ROW['sleep_quality'] == quality:
            yield ROW


def analytics_day_of_week_wake_up():
    grouped_day_of_week_df = df.groupby('day_of_week').agg({
        'wake_time': 'mean',
        'bedtime': 'mean'
    })


    grouped_day_of_week_df['bedtime'] = (grouped_day_of_week_df['bedtime']
                                         .apply(lambda x: datetime(1900, 1, 1) + x))

    # Жесточайший костыль
    max_row_bedtime = grouped_day_of_week_df[grouped_day_of_week_df['bedtime'] == np.max(grouped_day_of_week_df['bedtime'].values)]
    max_row_wake_time = grouped_day_of_week_df[grouped_day_of_week_df['wake_time'] == np.max(grouped_day_of_week_df['wake_time'].values)]

    print(max_row_bedtime)
    print(max_row_wake_time)

    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 7))
    ax[0].plot(grouped_day_of_week_df.index, grouped_day_of_week_df['wake_time'])
    ax[0].set_title('время подъема')
    ax[0].grid()

    ax[1].plot(grouped_day_of_week_df.index, grouped_day_of_week_df['bedtime'])
    ax[1].set_title('время отбоя')
    ax[1].grid()

    plt.show()

def analytics_count_of_qualities():
    grouped_quality_df = df.groupby('sleep_quality')['date'].count()

    quality_dict = grouped_quality_df.to_dict()

    categories = list(quality_dict.keys())
    values = list(quality_dict.values())

    plt.bar(categories, values)

    plt.title('Распределение качества сна')
    plt.xlabel('Качество сна')
    plt.ylabel('Частота')
    plt.show()


analytics_day_of_week_wake_up()