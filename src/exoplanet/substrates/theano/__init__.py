# -*- coding: utf-8 -*-


import theano
import warnings


if theano.config.floatX != "float64":
    warnings.warn(
        "exoplanet should only be used with 'float64' precision, "
        "but theano.config.floatX == '{0}'".format(theano.config.floatX)
    )