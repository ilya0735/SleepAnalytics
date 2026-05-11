from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import df
from src.utils import *

months_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

months_order = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
@logger
class AnalyticsByMonth:
    def __init__(self):

        df['month'] = df['date'].apply(lambda x: months_dict[x.month])

        df['month'] = pd.Categorical(df['month'], categories=months_order, ordered=True)

        self.grouped_mean_month_df = (df.groupby('month').agg({
            'wake_time': 'mean',
            'bedtime': 'mean',
            'total_sleep_hours': 'mean',
        }).sort_values('month', ascending=False))

        self.grouped_mean_month_df['bedtime'] = (self.grouped_mean_month_df['bedtime']
                                            .apply(lambda x: datetime(1900, 1, 1) + x))

        self.most_common_quality_by_month = (df.groupby(['month', 'sleep_quality'])
                                        .size()
                                        .reset_index(name='count')
                                        .sort_values('count', ascending=False)
                                        .drop_duplicates('month'))

    def max_row_bedtime(self):
        return self.grouped_mean_month_df.nlargest(1, 'bedtime')

    def max_row_wake_time(self):
        return self.grouped_mean_month_df.nlargest(1, 'wake_time')

    def max2_rows_total_sleep_hours(self):
        return self.grouped_mean_month_df.nlargest(2, 'total_sleep_hours')

    def max_row_sleep_quality(self):
        return self.most_common_quality_by_month[
            self.most_common_quality_by_month['sleep_quality'] == np.max(self.most_common_quality_by_month['sleep_quality'])]


    def min_row_bedtime(self):
        return self.grouped_mean_month_df.nsmallest(1, 'bedtime')

    def min_row_wake_time(self):
        return self.grouped_mean_month_df.nsmallest(1, 'wake_time')

    def min2_rows_total_sleep_hours(self):
        return self.grouped_mean_month_df.nsmallest(2, 'total_sleep_hours')

    def min_row_sleep_quality(self):
        return self.most_common_quality_by_month[
            self.most_common_quality_by_month['sleep_quality'] == np.min(self.most_common_quality_by_month['sleep_quality'])]

    @staticmethod
    def biggest_bedtime_deviation():
        dif_df = abs(df.groupby('month').agg({'bedtime': 'mean'}) - df['bedtime'].mean())
        return dif_df.nlargest(1, 'bedtime').reset_index()

    @staticmethod
    def biggest_wake_time_deviation():
        dif_df = abs(df.groupby('month').agg({'wake_time': 'mean'}) - df['wake_time'].mean())
        return dif_df.nlargest(1, 'wake_time').reset_index()

    @staticmethod
    def deviation_bedtime_graph():
        dif_df = abs(df.groupby('month').agg({'bedtime': 'mean'}) - df['bedtime'].mean())

        plt.figure(figsize=(10, 5))
        plt.plot(dif_df)
        plt.title('Суммарное время сна')
        plt.grid()
        plt.show()

    @staticmethod
    def deviation_wake_time_graph():
        dif_df = abs(df.groupby('month').agg({'wake_time': 'mean'}) - df['wake_time'].mean())

        plt.figure(figsize=(10, 5))
        plt.plot(dif_df)
        plt.title('Суммарное время сна')
        plt.grid()
        plt.show()

    def bedtime_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_month_df['bedtime'])
        plt.title('время отбоя')
        plt.grid()
        plt.show()

    def wake_time_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_month_df['wake_time'])
        plt.title('время подъема')
        plt.grid()
        plt.show()

    def total_sleep_hours_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_month_df['total_sleep_hours'])
        plt.title('Суммарное время сна')
        plt.grid()
        plt.show()

