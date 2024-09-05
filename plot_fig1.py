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

n_channels = 3


data_dir = expanduser('~/data/rsatoolbox/mur32/derivatives/figure1')

"""
rmds.h5
noise.npy
meta.json
"""

ds = load_dataset(join(data_dir, 'dataset.h5'))
ds_run0 = ds.split_obs('run')[0]
plt.figure()
ax = seaborn.heatmap(
    ds_run0.measurements[:n_channels, :5].T,
    annot=True, cbar=False, cmap='bone', vmin=-20, vmax=+20)
ax.set(xlabel='channels', ylabel='observations')
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.savefig('dataset.svg')
plt.close('all')



prec = numpy.load(join(data_dir, 'noise.npy')) # runs x vox x vox
prec_run0 = prec[0,:,:]
plt.figure()
ax = seaborn.heatmap(
    prec_run0[:n_channels, :n_channels],
    annot=True, cbar=False, cmap='bone', vmin=0, vmax=+0.01)
ax.set(xlabel='channels', ylabel='channels')
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.savefig('noise.svg')
plt.close('all')



rdms = load_rdm(join(data_dir, 'rdms.h5'))
plt.figure()
fig, _, _ = show_rdm(
    rdms,
    show_colorbar='panel'
)
plt.savefig('rdms.svg')
plt.close('all')