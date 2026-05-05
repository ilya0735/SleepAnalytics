from src.data_loader import df


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


for row in month_generator(month=2):
    print(row)

for row in day_of_week_generator(day='Monday'):
    print(row)

for row in sleep_quality_generator(quality='poor'):
    print(row)



