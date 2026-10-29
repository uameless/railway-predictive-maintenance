import numpy as np
import pandas as pd
from src.config import FAILURES

def event_mask(timestamps, intervals=FAILURES):
    """Reference intervals from UCI failure reports, not pointwise ground-truth labels."""
    ts = pd.to_datetime(timestamps)
    mask = np.zeros(len(ts),dtype=bool)
    for start,end in intervals:
        mask |= np.asarray((ts>=pd.Timestamp(start)) & (ts<=pd.Timestamp(end)))
    return mask

def summarize_alerts(timestamps,scores,threshold):
    """Descriptive alert counts inside/outside documented incident intervals."""
    mask = event_mask(timestamps)
    alerts = np.asarray(scores)>threshold
    return {'windows':len(alerts),'alerts_total':int(alerts.sum()),'alerts_in_reported_intervals':int((alerts&mask).sum()),'alerts_outside_reported_intervals':int((alerts&~mask).sum()),'reported_windows':int(mask.sum())}

def event_coverage(timestamps,scores,threshold,intervals=FAILURES):
    """Fraction of documented incident intervals with at least one alert during incident."""
    t = pd.to_datetime(timestamps)
    s = np.asarray(scores)
    records=[]
    for start,end in intervals:
        m=np.asarray((t>=pd.Timestamp(start))&(t<=pd.Timestamp(end)))
        records.append({'start':start,'end':end,'observed_windows':int(m.sum()),'detected':bool(np.any(s[m]>threshold)) if m.any() else None})
    return pd.DataFrame(records)
