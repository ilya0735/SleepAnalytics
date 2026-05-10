from matplotlib import pyplot as plt
from src.data_loader import df
from src.utils import logger


class AnalyticsByQualities:
    def __init__(self):
        self.grouped_quality_df = df.groupby('sleep_quality')['date'].count()
        self.quality_dict = self.grouped_quality_df.to_dict()


    @staticmethod
    def finding_the_period(sliced_df):
        try:
            arr = []
            for i in sliced_df.index:
                arr.append(i)

            arr_of_arr = []
            arr_to_append = []
            for i in range(0, len(arr) - 1):
                if arr[i + 1] - 1 == arr[i]:
                    arr_to_append.append(arr[i])
                else:
                    arr_of_arr.append(arr_to_append)
                    arr_to_append = []

            max_ordered_list = max(arr_of_arr, key=len)

            slice_ordered_df = df.iloc[max_ordered_list[0]:max_ordered_list[-1] + 1]

            return slice_ordered_df
        except ValueError:
            return 'Такой последовательности нет'

    @logger
    def good_period(self):
        sliced_df = df.loc[(df['sleep_quality'] == 'good')
                           | (df['sleep_quality'] == 'excellent')]

        return self.finding_the_period(sliced_df)

    @logger
    def not_bad_period(self):
        sliced_df = df.loc[(df['sleep_quality'] == 'good')
                         | (df['sleep_quality'] == 'excellent')
                         | (df['sleep_quality'] == 'average')]

        return self.finding_the_period(sliced_df)

    @logger
    def bad_period(self):
        sliced_df = df.loc[(df['sleep_quality'] == 'bad')
                           | (df['sleep_quality'] == 'very_bad')]

        return self.finding_the_period(sliced_df)


    @logger
    def max_quality_counts(self):
        return  max(self.quality_dict.items(), key=lambda x: x[1])

    @logger
    def max_quality_counts(self):
        return min(self.quality_dict.items(), key=lambda x: x[1])

    @logger
    def distribution_of_quality_graph(self):
        sleep_quality = list(self.quality_dict.keys())
        count = list(self.quality_dict.values())

        plt.bar(sleep_quality, count)

        plt.title('Распределение качества сна')
        plt.xlabel('Качество сна')
        plt.ylabel('Дни')

        plt.show()


ABQ = AnalyticsByQualities()
print(ABQ.bad_period())
