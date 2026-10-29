import numpy as np
import pandas as pd

def clean_data(frame):
    """Clean structural defects, preserving extreme sensor values for diagnosis."""
    df = frame.copy()
    df.columns = df.columns.str.strip()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    if df['timestamp'].isna().any():
        raise ValueError('Unparseable timestamps: investigate original CSV')
    df = df.sort_values('timestamp').drop_duplicates(subset=['timestamp'], keep='first').reset_index(drop=True)
    for col in df.columns.difference(['timestamp']):
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.replace([np.inf, -np.inf], np.nan)
    return df

def temporal_split(df, train_end='2020-03-31', val_end='2020-05-31'):
    """Disjoint chronological train/validation/test intervals."""
    t = pd.to_datetime(df['timestamp'])
    a = df.loc[t <= pd.Timestamp(train_end) + pd.Timedelta(days=1)-pd.Timedelta(nanoseconds=1)].copy()
    b = df.loc[(t > pd.Timestamp(train_end)+pd.Timedelta(days=1)-pd.Timedelta(nanoseconds=1)) & (t <= pd.Timestamp(val_end)+pd.Timedelta(days=1)-pd.Timedelta(nanoseconds=1))].copy()
    c = df.loc[t > pd.Timestamp(val_end)+pd.Timedelta(days=1)-pd.Timedelta(nanoseconds=1)].copy()
    if min(len(a),len(b),len(c)) == 0: raise ValueError('At least one chronological split is empty')
    return a,b,c
