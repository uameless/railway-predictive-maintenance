# Railway Predictive Maintenance Using Machine Learning

An end-to-end, reproducible exploratory machine learning project using real compressor sensor telemetry from the Porto metro (MetroPT-3).

## Business problem and objectives

Railway compressor degradation can cause delays and maintenance costs. We explore sensor behavior, engineer causal temporal features, compare a robust statistical baseline with Isolation Forest, and examine whether alerts coincide with documented incidents. A model alert is **not** automatically a failure prediction.

## Dataset

**Official UCI source:** https://archive.ics.uci.edu/dataset/791/metropt3+dataset

## Repository structure

- `notebooks/01...05`: EDA, cleaning, causal features, training, held-out evaluation.
- `src/data/`: loading; `src/preprocessing/`: cleaning and splitting.
- `src/features/`: minute-level temporal features.
- `src/models/`: fitting, scoring, saving, loading.
- `src/evaluation/`: descriptive incident-based assessment.
- `data/raw/`: original CSV (not tracked); `data/processed/`: generated features (not tracked); `models/`: generated fitted artifacts (not tracked)