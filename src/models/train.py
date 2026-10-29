import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import IsolationForest
from src.config import SEED

def fit_detector(features, contamination=0.01):
    """Fit unsupervised detector on chronological training observations only."""
    if not 0 < contamination <= 0.5: raise ValueError('Invalid contamination')
    model = Pipeline([('impute',SimpleImputer(strategy='median',add_indicator=False)),('scale',RobustScaler()),('detector',IsolationForest(n_estimators=150,contamination=contamination,random_state=SEED,n_jobs=-1))])
    model.fit(features)
    return model

def fit_statistical_baseline(features):
    """Train robust standardized distance baseline on training data."""
    med = features.median().fillna(0)
    mad = (features-med).abs().median().replace(0,np.nan).fillna(1)
    return {'median':med,'mad':mad}

def baseline_scores(features, baseline):
    """Higher score indicates larger robust deviation."""
    return ((features.fillna(baseline['median'])-baseline['median']).abs()/baseline['mad']).max(axis=1).to_numpy()

def save_model(model,path):
    """Persist trained model; only load artifacts from trusted sources."""
    path.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,path)
