
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas
import re
import sys
import glob
from ccdproc import CCDData

from goodman_pipeline.wcs import WCS

goodman_wcs = WCS()


class LineList(object):

    def __init__(self):
        self._pixels = []
        self._wavelength = []
        self._spectrum = []
        self._nist = None
        self._load_nist_list()

    def _load_nist_list(self, **kwargs):
        """Load all csv files from strong lines in nist."""
        nist_path = kwargs.get(
            'path',
            os.path.join(os.path.dirname(__import__('goodman_lamps').__file__),
                         'data/nist'))
        pandas_list = []

        assert os.path.isdir(nist_path)

        nist_files = glob.glob(os.path.join(nist_path, "*.txt"))

        for nist_file in nist_files:
            key = os.path.basename(nist_file)[22:-4]
            nist_data = pandas.read_csv(nist_file, names=['intensity',
                                                          'air_wavelength',
                                                          'spectrum',
                                                          'reference'])

            pandas_list.append(nist_data)
        self._nist = pandas.concat(pandas_list).reset_index(drop=True)
        # print(self._nist.to_string())

    def _get_spectrum_from_nist(self, wavelength):
        assert self._nist is not None
        sub_df = self._nist[np.isclose(self._nist.air_wavelength,
                                       wavelength,
                                       atol=1e-9,
                                       rtol=1e-9)]
        if not sub_df.empty and len(sub_df) == 1:
            return sub_df['spectrum'].item()
        elif len(sub_df) > 1:
            return ''
        else:
            return ''

    def import_from_file(self, ccd):
        for ang_key in ccd.header['GSP_A*']:
            pix_key = re.sub('GSP_A', 'GSP_P', ang_key)
            if int(float(ccd.header[ang_key])) != 0:
                pixel = float(ccd.header[pix_key])
                wavelength = float(ccd.header[ang_key])
                spectrum = self._get_spectrum_from_nist(wavelength=wavelength)

                self._pixels.append(pixel)
                self._wavelength.append(wavelength)
                self._spectrum.append(spectrum)


    @property
    def lines(self):
        for i in range(len(self._pixels)):
            yield self._pixels[i], self._wavelength[i], self._spectrum[i]

    # @property.setter
    # def lines(self, pixel, wavelength, spectrum):
    #     assert len(pixel) == len(wavelength)



def create_plot(mode):

    data_path = os.path.dirname(__import__('goodman_lamps').__file__)
    search_pattern = os.path.join(data_path,
                                  'data/lamps/*{:s}*.fits'.format(mode))
    print(data_path)
    print(search_pattern)

    for file_name in glob.glob(search_pattern):
        fig, ax = plt.subplots(figsize=(16, 7))

        ccd = CCDData.read(file_name, unit='adu')
        line_list = LineList()
        line_list.import_from_file(ccd=ccd)

        wavelength, intensity = goodman_wcs.read_gsp_wcs(ccd=ccd)

        top_lim = 1.4 * ccd.data.max()
        bottom_lim = ccd.data.min() - 0.05 * ccd.data.max()
        plt.ylim((bottom_lim, top_lim))
        plt.xlim((wavelength[0], wavelength[-1]))

        ax.set_title('{:s} - {:s}'.format(ccd.header['object'],
                                          ccd.header['wavmode']))
        ax.set_xlabel('Wavelength (Angstrom)')
        ax.set_ylabel('Intensity (ADU)')
        ax.plot(wavelength, intensity)

        for pixel, wavelength, spectrum in line_list.lines:
            text = '{:.4f} - {:s}'.format(wavelength, spectrum)
            print(text)
            plt.axvline(wavelength, alpha=0.1, color='k')

            text_x = wavelength
            text_y = np.max((ccd.data[int(np.floor(pixel))],
                             ccd.data[int(np.ceil(pixel))]))

            y_offset = 0.05 * ccd.data.max()

            plt.text(text_x, text_y + y_offset, text, rotation=90,
                     verticalalignment='bottom',
                     horizontalalignment='center')

        plt.tight_layout()
        plt.show()


# print(dir(__import__('goodman_lamps').__file__))
# # for mod in sys.modules:
# #
# #     print(mod)
if __name__ == '__main__':

    create_plot('1200M1')



