from src.analysis.analytics_by_day_of_week import AnalyticsByDayOfWeek
from src.analysis.analytics_by_month import AnalyticsByMonth
from src.analysis.analytics_by_qualities import AnalyticsByQualities
from src.utils import row_generator
from src.data_loader import df
week_analysis = AnalyticsByDayOfWeek()
month_analysis = AnalyticsByMonth()
quality_analysis = AnalyticsByQualities()

def display_most_important():
    print("===========================================================================================================")
    print("Лучший день недели по качеству сна в среднем")
    print(f"День недели: {week_analysis.max_row_sleep_quality()['day_of_week'].iloc[0]}")
    print(f"Качество сна: {week_analysis.max_row_sleep_quality()['sleep_quality'].iloc[0]}")
    print("===========================================================================================================")
    print()
    print("===========================================================================================================")
    print("Худший день недели по качеству сна в среднем")
    print(f"День недели: {week_analysis.min_row_sleep_quality()['day_of_week'].iloc[0]}")
    print(f"Качество сна: {week_analysis.min_row_sleep_quality()['sleep_quality'].iloc[0]}")
    print("===========================================================================================================")
    print()
    print("===========================================================================================================")
    print("Месяц с самым большим отклонением по отходу ко сну")
    print(f"Месяц: {month_analysis.biggest_bedtime_deviation()['month'].iloc[0]}")
    time = month_analysis.biggest_bedtime_deviation()['bedtime'].iloc[0]
    print(f"Отклонение: {time.components.hours:02}:{time.components.minutes:02}:{time.components.seconds:02}")
    print("===========================================================================================================")
    print()
    print("===========================================================================================================")
    print("Месяц с самым большим отклонением по подъёму")
    print(f"Месяц: {month_analysis.biggest_wake_time_deviation()['month'].iloc[0]}")
    time = month_analysis.biggest_wake_time_deviation()['wake_time'].iloc[0]
    print(f"Отклонение: {time.components.hours:02}:{time.components.minutes:02}:{time.components.seconds:02}")
    print("===========================================================================================================")
    print()
    print("===========================================================================================================")
    print("Самый длинный хороший период")
    if quality_analysis.good_period() is not str:
        print(quality_analysis.good_period()[['date', 'total_sleep_hours','sleep_quality']])
    else:
        print(quality_analysis.good_period())
    print("===========================================================================================================")
    print()
    print("===========================================================================================================")
    print("Самый длинный неплохой период")
    if quality_analysis.good_period() is not str:
        print(quality_analysis.not_bad_period()[['date', 'total_sleep_hours', 'sleep_quality']])
    else:
        print(quality_analysis.not_bad_period())
    print("===========================================================================================================")

def show_rows(generator, df):
    gen = generator(df)
    for row in gen:
        print(row)
        user_input = input("Enter - дальше, любое значение - стоп: ")
        if user_input != "":
            break






