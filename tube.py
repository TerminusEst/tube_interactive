import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
from scipy import sparse
from utils import *


def read_panels():
        # read data files, return panels, and alphabetised stations list
        tube_pd = pd.read_csv('data/Inter_station_database.csv')
        tube_pd['Colour'] = tube_pd.apply(lambda row: add_colour(row['Line']),axis=1)

        lats = pd.read_csv('data/stations.csv')
        lats['name']=lats['name'].str.upper()

        stations = set(np.concatenate((tube_pd['Station from'].values, tube_pd['Station to'].values)))

        stations = list(stations)

        stations.sort()

        return tube_pd, lats, stations
