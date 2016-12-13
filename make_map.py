import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
from utils import *
from tube import *
from bokeh_scatter import *

#plt.style.use('fivethirtyeight')


def embed(dist, df, stations):

        seed = 123

        mds = manifold.MDS(n_components=2, 
                max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)

        pos = mds.fit(dist).embedding_
	rot_pos = np.zeros_like(pos)
	rot_pos[:,0] = pos[:,1]
	rot_pos[:,1] = -1 * pos[:,0]
        
        stat_col = []
        stat_x   = []
        stat_y   = []    
        for i, station in enumerate(stations):

                if station in tube_df['Station from'].values:
                        stat_col.append(
                  tube_df[tube_df['Station from'] == station].Colour.values[0])
                else:
                        stat_col.append(
                  tube_df[tube_df['Station to'] == station].Colour.values[0])


                stat_x.append(rot_pos[i, 0])

                stat_y.append(rot_pos[i, 1])
        
        d = {'Name':stations, 'X':stat_x, 'Y':stat_y, 'Colour':stat_col}
        
        return pd.DataFrame(d)

if __name__ == '__main__':

        dist = np.loadtxt('data/dist_mat.csv', delimiter=',')

        tube_df, lats, stations = read_panels()

        stat_df = embed(dist, tube_df, stations)

        bokeh_scatter(stat_df)
