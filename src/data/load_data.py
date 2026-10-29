import pandas as pd
from src.config import RAW

def load_raw(path=RAW):
    """Load original UCI CSV without altering source observations."""
    if not path.exists():
        raise FileNotFoundError(f'Missing {path}. Download MetroPT-3 from https://archive.ics.uci.edu/dataset/791/metropt3+dataset and extract CSV into data/raw/.')
    df = pd.read_csv(path, low_memory=False)
    if 'timestamp' not in df:
        raise ValueError('Expected timestamp column not found')
    return df
