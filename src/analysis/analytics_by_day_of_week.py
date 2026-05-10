from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from src.data_loader import df
from src.utils import *


@logger
class AnalyticsByDayOfWeek:
    def __init__(self):
        self.grouped_mean_day_of_week_df = df.groupby('day_of_week').agg({
            'wake_time': 'mean',
            'bedtime': 'mean',
            'total_sleep_hours': 'mean',
        })

        self.grouped_mean_day_of_week_df['bedtime'] = (self.grouped_mean_day_of_week_df['bedtime']
                                                  .apply(lambda x: datetime(1900, 1, 1) + x))

        self.most_common_quality_by_day = (df.groupby(['day_of_week', 'sleep_quality'])
                                           .size()
                                           .reset_index(name='count')
                                           .sort_values('count', ascending=False)
                                           .drop_duplicates('day_of_week')
                                           .sort_values('day_of_week'))


    def max_row_bedtime(self):
        return self.grouped_mean_day_of_week_df.nlargest(1, 'bedtime')

    def max_row_wake_time(self):
        return self.grouped_mean_day_of_week_df.nlargest(1, 'wake_time')

    def max2_rows_total_sleep_hours(self):
        return self.grouped_mean_day_of_week_df.nlargest(2, 'total_sleep_hours')

    def max_row_sleep_quality(self):
        return self.most_common_quality_by_day[
            self.most_common_quality_by_day['sleep_quality'] == np.max(self.most_common_quality_by_day['sleep_quality'])]


    def min_row_bedtime(self):
        return self.grouped_mean_day_of_week_df.nsmallest(1, 'bedtime')

    def min_row_wake_time(self):
        return self.grouped_mean_day_of_week_df.nsmallest(1, 'wake_time')

    def min2_rows_total_sleep_hours(self):
        return self.grouped_mean_day_of_week_df.nsmallest(2, 'total_sleep_hours')

    def min_row_sleep_quality(self):
        return self.most_common_quality_by_day[
            self.most_common_quality_by_day['sleep_quality'] == np.min(self.most_common_quality_by_day['sleep_quality'])]


    def bedtime_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_day_of_week_df['bedtime'])
        plt.title('время отбоя')
        plt.grid()
        plt.show()

    def wake_time_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_day_of_week_df['wake_time'])
        plt.title('время подъема')
        plt.grid()
        plt.show()

    def total_sleep_hours_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.grouped_mean_day_of_week_df['total_sleep_hours'])
        plt.title('Суммарное время сна')
        plt.grid()
        plt.show()
