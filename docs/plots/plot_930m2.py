from __future__ import absolute_import

from goodman_lamps.goodman_lamps import create_plot


def dark_theme():
    create_plot(mode='930M2', dark=True)


def light_theme():
    create_plot(mode='930M2', dark=False)