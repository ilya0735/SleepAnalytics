import pandas as pd
from src.data_loader import DataLoader


def make_file(tmp_path):
    df = pd.DataFrame({
        "date": ["2024-01-01", "2024-01-02"],
        "day_of_week": ["Monday", "Tuesday"],
        "bedtime": ["22:30", "06:30"],
        "wake_time": ["06:30", "14:00"],
        "total_sleep_hours": [8.0, 7.5],
        "deep_sleep_hours": [2.0, 1.5],
        "rem_sleep_hours": [1.5, 2.0],
        "awakenings": [1, 2],
        "sleep_quality": ["good", "average"],
    })

    file = tmp_path / "data.csv"
    df.to_csv(file, index=False)

    return file


def test_load(tmp_path):
    file = make_file(tmp_path)

    dl = DataLoader(file)
    df = dl.df

    assert len(df) == 2
    assert "date" in df.columns


def test_columns(tmp_path):
    file = make_file(tmp_path)

    dl = DataLoader(file)
    df = dl.df

    expected = [
        "date",
        "day_of_week",
        "bedtime",
        "wake_time",
        "total_sleep_hours",
        "deep_sleep_hours",
        "rem_sleep_hours",
        "awakenings",
        "sleep_quality",
    ]

    for col in expected:
        assert col in df.columns


def test_values(tmp_path):
    file = make_file(tmp_path)

    dl = DataLoader(file)
    df = dl.df

    assert df["awakenings"].iloc[0] == 1
    assert df["sleep_quality"].iloc[0] == "good"


def test_shape(tmp_path):
    file = make_file(tmp_path)

    dl = DataLoader(file)
    df = dl.df

    assert df.shape == (2, 9)


def test_types(tmp_path):
    file = make_file(tmp_path)

    dl = DataLoader(file)
    df = dl.df

    assert "day_of_week" in df.columns
    assert "sleep_quality" in df.columns