import joblib

def load_model(path):
    """Load a trusted local fitted pipeline."""
    if not path.exists(): raise FileNotFoundError(path)
    return joblib.load(path)

def anomaly_scores(model, features):
    """Higher values correspond to more anomalous windows."""
    return -model.decision_function(features)
