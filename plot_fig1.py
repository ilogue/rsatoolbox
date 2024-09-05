"""Plot various parts for figure 1

See prep_fig1.py


"""
from os.path import expanduser, join
from rsatoolbox.data.dataset import load_dataset
from rsatoolbox.rdm.rdms import load_rdm
from rsatoolbox.vis.rdm_plot import show_rdm
import numpy
import seaborn
import matplotlib.pyplot as plt

n_channels = 5
data_cmap = 'mako'
conditions = ['image_bagel', 'image_glove', 'image_kettle',
              'text_bagel', 'text_glove', 'text_kettle']
voxel_selection = []


data_dir = expanduser('~/data/rsatoolbox/mur32/derivatives/figure1')

"""
rmds.h5
noise.npy
meta.json
"""

ds = load_dataset(join(data_dir, 'dataset.h5'))
ds_run0 = ds.split_obs('run')[0]
ds_run0 = ds_run0.subset_obs('condition', conditions)
plt.figure()
ax = seaborn.heatmap(
    ds_run0.measurements[:, :n_channels],
    annot=True, cbar=False, square=True, cmap=data_cmap, vmin=-20, vmax=+20)
ax.set(xlabel='channels', ylabel='observations')
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.savefig('dataset.svg')
plt.close('all')



prec = numpy.load(join(data_dir, 'noise.npy')) # runs x vox x vox
prec_run0 = prec[0,:,:]
plt.figure()
ax = seaborn.heatmap(
    prec_run0[:n_channels, :n_channels],
    annot=True, cbar=False, square=True, cmap=data_cmap, vmin=0, vmax=+0.025)
ax.set(xlabel='channels', ylabel='channels')
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.savefig('prec.svg')
plt.close('all')



rdms = load_rdm(join(data_dir, 'rdms.h5'))
rdms = rdms.subsample_pattern('condition', conditions)
plt.figure()
fig, _, _ = show_rdm(
    rdms,
    show_colorbar='panel'
)
plt.savefig('rdms.svg')
plt.close('all')