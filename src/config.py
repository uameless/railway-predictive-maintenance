from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw' / 'MetroPT3(AirCompressor).csv'
PROCESSED = ROOT / 'data' / 'processed'
MODELS = ROOT / 'models'
SEED = 42
ANALOG = ['TP2','TP3','H1','DV_pressure','Reservoirs','Oil_temperature','Motor_current']
DIGITAL = ['COMP','DV_electric','TOWERS','MPG','LPS','Pressure_switch','Oil_level','Caudal_impulses']
FAILURES = [('2020-04-18 00:00','2020-04-18 23:59'),('2020-05-29 23:30','2020-05-30 06:00'),('2020-06-05 10:00','2020-06-07 14:30'),('2020-07-15 14:30','2020-07-15 19:00')]
