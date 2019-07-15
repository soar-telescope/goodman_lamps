.. Reference Lamps Library documentation master file, created by
   sphinx-quickstart on Thu Sep 13 12:52:15 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Reference Lamps Library's documentation!
===================================================

.. image:: https://readthedocs.org/projects/goodman-lamps/badge/?version=latest
    :target: https://goodman-lamps.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This is a visual library of all the usable lamps of the Goodman High Throughput
Spectrograph.

.. note::

   The plots in this library are automatically generated therefore in some cases
   if two lines are too close together the labels will appear stacked


The table below is presented as a quick reference. It is not generated automatically.

To see a full set of plots of all lamps please visit this `GitHub Repository <https://github.com/simontorres/general_documentation/tree/master/jupyter-notebooks/pipeline_development/lamp-usability>`_

.. table:: Lamp usability per spectroscopic mode

   ========== ========== ========== ========== ========== ========== ========== ==========
      Mode      Filter       Ne        HgAr      HgArNe     CuHeAr     FeHeAr       Ar
   ========== ========== ========== ========== ========== ========== ========== ==========
    400 M1        --         No         Yes        Yes        No         No          No
    400 M2      GG-450       Yes        Yes        Yes        Yes        Yes         Yes
    600 UV        --         No         Yes        Yes        Yes        No          No
    600 Blue      --         No         Yes        Yes        Yes        No          No
    600 Mid     GG-385       No         Yes        Yes        Yes        No          No
    600 Red     GG-495       Yes        Yes        Yes        Yes        Yes         Yes
    930 M1        --         No         Yes        Yes        No         No          No
    930 M2        --         No         Yes        Yes        Yes        Yes         Yes
    930 M3      GG-385       No         No         No         Yes        Yes         No
    930 M4      GG-495       Yes        Yes        Yes        Yes        No          No
    930 M5      GG-495       Yes        Yes        Yes        Yes        Yes         Yes
    930 M6      OG-570       Yes        Yes        Yes        Yes        Yes         Yes
    1200 M0       --         No         No         No         No         No          No
    1200 M1       --         No         No         No         Yes        Yes         Yes
    1200 M2       --         No         No         No         Yes        Yes         No
    1200 M3       --         No         No         No         Yes        Yes         No
    1200 M4     GG-455       Yes        No         Yes        Yes        Yes         No
    1200 M5     GG-455       Yes        Yes        Yes        Yes        Yes         Yes
    1200 M6     GG-495       Yes        Yes        Yes        Yes        Yes         Yes
    1200 M7     OG-570       Yes        Yes        Yes        Yes        Yes         Yes
   ========== ========== ========== ========== ========== ========== ========== ==========





.. toctree::
   :maxdepth: 2
   :caption: Plots

   plots_400
   plots_600
   plots_930
   plots_1200


.. toctree::
   :maxdepth: 2
   :caption: About

   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
