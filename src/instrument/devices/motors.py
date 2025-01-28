"""
Custom Motor Classes.
"""

import logging

from apstools.utils import dynamic_import
from ophyd import Component
from ophyd import EpicsMotor
from ophyd import EpicsSignal

logger = logging.getLogger(__name__)
logger.bsdev(__file__)


class EpicsMotor_SREV(EpicsMotor):
    """Provide access to motor steps/revolution configuration."""

    steps_per_revolution = Component(EpicsSignal, ".SREV", kind="config")


def declare_motors(*, class_name="ophyd.EpicsMotor", prefix=None, first=1, last=1):
    """Create one or more motor objects."""
    # FIXME: This function returns `None` to guarneri.Instrument.
    klass = dynamic_import(class_name)
    n = min(first, last)
    while n <= max(first, last):
        klass(f"{prefix}{n}", name=f"m{n}")
        n += 1
