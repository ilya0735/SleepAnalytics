from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import df
from src.utils import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


@logger
def analytics_by_day_of_week():
    grouped_mean_day_of_week_df = df.groupby('day_of_week').agg({
        'wake_time': 'mean',
        'bedtime': 'mean',
        'total_sleep_hours': 'mean',
    })



    grouped_mean_day_of_week_df['bedtime'] = (grouped_mean_day_of_week_df['bedtime']
                                         .apply(lambda x: datetime(1900, 1, 1) + x))


    # Жесточайший костыль для нумпая в коде
    max_row_bedtime = grouped_mean_day_of_week_df[grouped_mean_day_of_week_df['bedtime'] == np.max(grouped_mean_day_of_week_df['bedtime'].values)]
    max_row_wake_time = grouped_mean_day_of_week_df[grouped_mean_day_of_week_df['wake_time'] == np.max(grouped_mean_day_of_week_df['wake_time'].values)]
    max2_rows_wake_time = grouped_mean_day_of_week_df.nlargest(2, 'total_sleep_hours')

    min_row_bedtime = grouped_mean_day_of_week_df[grouped_mean_day_of_week_df['bedtime'] == np.min(grouped_mean_day_of_week_df['bedtime'].values)]
    min_row_wake_time = grouped_mean_day_of_week_df[grouped_mean_day_of_week_df['wake_time'] == np.min(grouped_mean_day_of_week_df['wake_time'].values)]
    min2_rows_wake_time = grouped_mean_day_of_week_df.nsmallest(2, 'total_sleep_hours')

    # print(max_row_bedtime)
    # print(max_row_wake_time)
    #
    # print(min_row_bedtime)
    # print(min_row_wake_time)

    print(min2_rows_wake_time)


    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(8, 10))
    ax[0].plot(grouped_mean_day_of_week_df.index, grouped_mean_day_of_week_df['wake_time'])
    ax[0].set_title('время подъема')
    ax[0].grid()

    ax[1].plot(grouped_mean_day_of_week_df.index, grouped_mean_day_of_week_df['bedtime'])
    ax[1].set_title('время отбоя')
    ax[1].grid()

    ax[2].plot(grouped_mean_day_of_week_df.index, grouped_mean_day_of_week_df['total_sleep_hours'])
    ax[2].set_title('Суммарное время сна')
    ax[2].grid()

    plt.show()


@logger
def analytics_by_qualities():
    grouped_quality_df = df.groupby('sleep_quality')['date'].count()

    quality_dict = grouped_quality_df.to_dict()

    max_counts = max(quality_dict.items(), key=lambda x: x[1])
    min_counts = min(quality_dict.items(), key=lambda x: x[1])

    print(max_counts, min_counts)

    sleep_quality = list(quality_dict.keys())
    count = list(quality_dict.values())

    plt.bar(sleep_quality, count)

    plt.title('Распределение качества сна')
    plt.xlabel('Качество сна')
    plt.ylabel('Дни')

    plt.show()


analytics_by_qualities()

