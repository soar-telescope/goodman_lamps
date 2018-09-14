from __future__ import absolute_import

import glob

from goodman_lamps.tools.create_plot import create_plot

if __name__ == '__main__':
    files = glob.glob(
        '/data/simon/development/soar/goodman-lamps-lib/goodman_lamps/data/lamps/*400M2*fits')
    for _file in files:
        create_plot(_file)