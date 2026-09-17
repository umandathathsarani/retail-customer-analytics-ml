# Decision Log

Record important decisions throughout the project lifecycle.

## Decision 1: Baseline Segmentation Model

### Options Considered
* Baseline K-Means (K=3)
* RFM Quantile Hard-coding (e.g., 3x3x3 grid)
* Baseline Hierarchical Clustering

### Selected Option
* Baseline K-Means (K=3)

### Reason
* Highly interpretable (often categorizing into High, Medium, Low segments).
* Computationally fast.
* Provides a standard mathematical metric (Silhouette score) to use as a benchmark against optimal K searches and alternative algorithms (like DBSCAN).

### Evidence
* RFM variables are continuous. Quantile grouping discretization discards variance information, whereas K-Means uses the full variance space (after log transformation and scaling).

### Trade-offs
* Pre-defines K=3 which may not actually be the natural grouping of the data.
* Assumes spherical clusters.

### Date
* 2026-09-17
