# MetroPT-3 data setup

1. Visit https://archive.ics.uci.edu/dataset/791/metropt3+dataset.
2. Download the official archive (~208.3 MB); no download is performed automatically.
3. Extract `MetroPT3(AirCompressor).csv` to `data/raw/` (exact filename).
4. Keep `Data Description_Metro.pdf` in `data/raw/` if downloaded.
5. Do not commit raw or processed data. The CSV has approximately 1,516,948 observations and 15 sensor signals.

**Attribution:** Davari, N., Veloso, B., Ribeiro, R., & Gama, J. (2021). MetroPT-3 Dataset. UCI Machine Learning Repository. DOI: 10.24432/C5VW3R. License: CC BY 4.0 (credit required).

**Important:** UCI lists both 1 Hz and 0.1 Hz in different descriptions; measure the actual timestamp deltas rather than assuming a fixed cadence. The dataset has no row-level fault labels; UCI provides four incident intervals.
