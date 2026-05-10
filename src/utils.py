import time
from functools import wraps
import logging
from pathlib import Path

base = Path(__file__).resolve().parent.parent
path_to_log_data = base / 'logs' / 'logs.log'

logging.basicConfig(
    filename=path_to_log_data,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'called {func.__name__}')
        try:
            result = func(*args, **kwargs)
            logging.info(f'finished {func.__name__}')
            return result
        except Exception as e:
            logging.error(f'failed {func.__name__}: {e}')
            raise
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f'{func.__name__} worked {execution_time:.4f} seconds')
        return result
    return wrapper


def month_generator(df, month):
    for i, ROW in df.iterrows():
        if ROW['date'].month == month:
            yield ROW

def day_of_week_generator(df, day):
    for i, ROW in df.iterrows():
        if ROW['day_of_week'] == day:
            yield ROW

def sleep_quality_generator(df, quality):
    for i, ROW in df.iterrows():
        if ROW['sleep_quality'] == quality:
            yield ROW





