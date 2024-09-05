"""Plot various parts for figure 1

See prep_fig1.py

todo

- rotate
- axis labels
"""
from os.path import expanduser, join
from rsatoolbox.data.dataset import load_dataset
import seaborn
import matplotlib.pyplot as plt


data_dir = expanduser('~/data/rsatoolbox/mur32/derivatives/figure1')

"""
dataset.h5
rmds.h5
noise.npy
meta.json
"""

ds = load_dataset(join(data_dir, 'dataset.h5'))
ds_run0 = ds.split_obs('run')[0]
plt.figure()
seaborn.heatmap(ds_run0.measurements[:3, :5], annot=True)
plt.savefig('dataset.svg')
plt.close('all')