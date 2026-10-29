import pandas as pd
from src.config import ANALOG, DIGITAL

def make_features(df, window=12):
    """Generate causal features on 1-minute past-only aggregates.

    Each timestamp represents the END of its minute. Windows never use future data.
    Call separately for each temporal split to prevent cross-boundary feature mixing.
    """
    columns = [c for c in ANALOG + DIGITAL if c in df.columns]
    if not columns: raise ValueError('No recognized sensor columns')
    data = df.set_index('timestamp')[columns].sort_index()
    minute = data.resample('1min', label='right', closed='right').mean()
    out = minute.add_suffix('_mean')
    for col in [c for c in ANALOG if c in minute]:
        past = minute[col].shift(1)
        out[f'{col}_lag1'] = past
        out[f'{col}_rolling_mean'] = past.rolling(window, min_periods=window).mean()
        out[f'{col}_rolling_std'] = past.rolling(window, min_periods=window).std()
        out[f'{col}_rolling_min'] = past.rolling(window, min_periods=window).min()
        out[f'{col}_rolling_max'] = past.rolling(window, min_periods=window).max()
        out[f'{col}_delta'] = minute[col].diff()
    return out.dropna(how='all').reset_index()
