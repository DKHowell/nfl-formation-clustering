# nfl-formation-clustering

This project is an exploration of defensive player formations and their effect on play success using NFL play-by-play and player tracking data. Player starting positions are transformed into low-dimensional embeddings and clustered. Cluster assignments and other features are then examined to determine their relationship with offensive play success. A full report detailing the data, methodology, and results can be found [here](https://github.com/DKHowell/nfl-formation-clustering/blob/main/NFL_Clustering_Report.pdf).

## Files

1. Data can be found [here](https://github.com/DKHowell/nfl-formation-clustering/tree/main/Data)
2. Data cleaning, clustering, and initial exploration is performed in this [Jupyter notebook](https://github.com/DKHowell/nfl-formation-clustering/blob/main/NFL_defense_clustering.ipynb)
3. Further analysis is performed using R [here](https://github.com/DKHowell/nfl-formation-clustering/blob/main/ClusterAnalysis.md)
4. [Final report](https://github.com/DKHowell/nfl-formation-clustering/blob/main/NFL_Clustering_Report.pdf)

### Dependencies

* Python:
  * Python dependencies can be found [here](https://github.com/DKHowell/nfl-formation-clustering/blob/main/environment.yml)
* R:
  * R - 4.1.0
  * jtools
  * glmnet
  * car

### Executing program

Create conda environment 

```
conda env create -f environment.yml
```

Activate conda environment

```
conda activate nfl-clustering
```

To run Jupyter notebook, use command:

```
jupyter run NFL_defense_clustering.ipynb
```
