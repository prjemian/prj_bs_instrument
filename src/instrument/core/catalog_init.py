"""
Databroker catalog, provides ``cat``
====================================

.. autosummary::
    ~cat
"""

import logging

import databroker

from ..utils.config_loaders import iconfig

logger = logging.getLogger(__name__)
logger.bsdev(__file__)

TEMPORARY_CATALOG_NAME = "temp"

catalog_name = iconfig.get("DATABROKER_CATALOG", TEMPORARY_CATALOG_NAME)

try:
    _cat = databroker.catalog[catalog_name]
except KeyError:
    _cat = databroker.temp()

cat = _cat.v2
"""Databroker catalog object, receives new data from ``RE``."""

logger.info("Databroker catalog: %s", cat.name)
