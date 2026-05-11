import pandas as pd
from src.analysis.analytics_by_day_of_week import AnalyticsByDayOfWeek
from src.analysis.analytics_by_month import AnalyticsByMonth
from src.analysis.analytics_by_qualities import AnalyticsByQualities


class SleepAnalyticsMenu:
    def __init__(self):
        print("Инициализация данных. Пожалуйста, подождите...")
        self.day_analytics = AnalyticsByDayOfWeek()
        self.month_analytics = AnalyticsByMonth()
        self.qualities_analytics = AnalyticsByQualities()

    def display_result(self, title, result):
        print(f"\n{'=' * 60}")
        print(f" {title} ".center(60, '*'))
        print(f"{'=' * 60}")

        if isinstance(result, pd.DataFrame) or isinstance(result, pd.Series):
            if result.empty:
                print("Данные отсутствуют или пусты.")
            else:
                print(result.to_string())
        else:
            print(result)

        print(f"{'=' * 60}\n")

    def display_graph(self, graph_method):
        choice = input("Хотите посмотреть график по этим данным? (y/n / д/н): ").strip().lower()
        if choice in ['y', 'yes', 'д', 'да']:
            print("Отрисовка графика...")
            graph_method()

    def main_menu(self):
        while True:
            print("\n" + "#" * 30)
            print(" ГЛАВНОЕ МЕНЮ АНАЛИТИКИ СНА ")
            print("#" * 30)
            print("1. Аналитика по дням недели")
            print("2. Аналитика по месяцам")
            print("3. Аналитика по качеству сна")
            print("0. Выход")

            choice = input("\nВыберите раздел: ").strip()

            if choice == '1':
                self.menu_day_of_week()
            elif choice == '2':
                self.menu_month()
            elif choice == '3':
                self.menu_qualities()
            elif choice == '0':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный ввод. Попробуйте еще раз.")

    def menu_day_of_week(self):
        while True:
            print("\n--- АНАЛИТИКА ПО ДНЯМ НЕДЕЛИ ---")
            print("1. Время отбоя (Самое позднее и самое раннее)")
            print("2. Время подъема (Самое позднее и самое раннее)")
            print("3. Суммарное время сна (Максимум и минимум)")
            print("4. Качество сна (Лучшее и худшее)")
            print("0. Вернуться в главное меню")

            choice = input("\nВыберите действие: ").strip()

            if choice == '1':
                self.display_result("Самое позднее время отбоя", self.day_analytics.max_row_bedtime())
                self.display_result("Самое раннее время отбоя", self.day_analytics.min_row_bedtime())
                self.display_graph(self.day_analytics.bedtime_graph)

            elif choice == '2':
                self.display_result("Самое позднее время подъема", self.day_analytics.max_row_wake_time())
                self.display_result("Самое раннее время подъема", self.day_analytics.min_row_wake_time())
                self.display_graph(self.day_analytics.wake_time_graph)

            elif choice == '3':
                self.display_result("Максимальное время сна", self.day_analytics.max2_rows_total_sleep_hours())
                self.display_result("Минимальное время сна", self.day_analytics.min2_rows_total_sleep_hours())
                self.display_graph(self.day_analytics.total_sleep_hours_graph)

            elif choice == '4':
                self.display_result("Лучшее качество сна по дням", self.day_analytics.max_row_sleep_quality())
                self.display_result("Худшее качество сна по дням", self.day_analytics.min_row_sleep_quality())

            elif choice == '0':
                break
            else:
                print("Неверный ввод.")

    def menu_month(self):
        while True:
            print("\n--- АНАЛИТИКА ПО МЕСЯЦАМ ---")
            print("1. Время отбоя (Самое позднее и самое раннее)")
            print("2. Время подъема (Самое позднее и самое раннее)")
            print("3. Суммарное время сна (Максимум и минимум)")
            print("4. Качество сна (Лучшее и худшее)")
            print("5. Наибольшие отклонения (Отбой и Подъем)")
            print("0. Вернуться в главное меню")

            choice = input("\nВыберите действие: ").strip()

            if choice == '1':
                self.display_result("Самое позднее время отбоя (Месяц)", self.month_analytics.max_row_bedtime())
                self.display_result("Самое раннее время отбоя (Месяц)", self.month_analytics.min_row_bedtime())
                self.display_graph(self.month_analytics.bedtime_graph)

            elif choice == '2':
                self.display_result("Самое позднее время подъема (Месяц)", self.month_analytics.max_row_wake_time())
                self.display_result("Самое раннее время подъема (Месяц)", self.month_analytics.min_row_wake_time())
                self.display_graph(self.month_analytics.wake_time_graph)

            elif choice == '3':
                self.display_result("Максимальное время сна (Месяц)",
                                    self.month_analytics.max2_rows_total_sleep_hours())
                self.display_result("Минимальное время сна (Месяц)", self.month_analytics.min2_rows_total_sleep_hours())
                self.display_graph(self.month_analytics.total_sleep_hours_graph)

            elif choice == '4':
                self.display_result("Лучшее качество сна по месяцам", self.month_analytics.max_row_sleep_quality())
                self.display_result("Худшее качество сна по месяцам", self.month_analytics.min_row_sleep_quality())

            elif choice == '5':
                self.display_result("Наибольшее отклонение по времени отбоя",
                                    AnalyticsByMonth.biggest_bedtime_deviation())
                self.display_graph(AnalyticsByMonth.deviation_bedtime_graph)

                self.display_result("Наибольшее отклонение по времени подъема",
                                    AnalyticsByMonth.biggest_wake_time_deviation())
                self.display_graph(AnalyticsByMonth.deviation_wake_time_graph)

            elif choice == '0':
                break
            else:
                print("Неверный ввод.")

    def menu_qualities(self):
        while True:
            print("\n--- АНАЛИТИКА ПО КАЧЕСТВУ СНА ---")
            print("1. Найти лучший период сна (good/excellent)")
            print("2. Найти нормальный период сна (good/excellent/average)")
            print("3. Найти худший период сна (bad/very_bad)")
            print("4. Показать самое частое качество сна")
            print("5. График распределения качества сна")
            print("0. Вернуться в главное меню")

            choice = input("\nВыберите действие: ").strip()

            if choice == '1':
                self.display_result("Самый продолжительный период хорошего сна", self.qualities_analytics.good_period())
            elif choice == '2':
                self.display_result("Самый продолжительный период неплохого сна",
                                    self.qualities_analytics.not_bad_period())
            elif choice == '3':
                self.display_result("Самый продолжительный период плохого сна", self.qualities_analytics.bad_period())
            elif choice == '4':
                self.display_result("Самое часто встречающееся качество", self.qualities_analytics.max_quality_counts())
            elif choice == '5':
                self.qualities_analytics.distribution_of_quality_graph()
            elif choice == '0':
                break
            else:
                print("Неверный ввод.")
