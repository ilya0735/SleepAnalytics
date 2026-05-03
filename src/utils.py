import time
from functools import wraps
import logging



logging.basicConfig(
    filename='logging_info.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
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
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.4f} секунд")
        logging.info(f'{func.__name__} worked {execution_time:.4f} seconds')
        return result
    return wrapper
