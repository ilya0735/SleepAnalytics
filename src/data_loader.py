import pandas as pd
from pathlib import Path

current_dir = Path.cwd()
path = current_dir.parent / 'data' / 'sleep_dataset.csv'

print(path)





# dataset = pd.read_csv('data/sleep_dataset.csv')
# print(dataset.head())
# print(dataset.describe())