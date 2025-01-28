"""
Diffractometers

https://github.com/prjemian/epics-docker/tree/main/v1.1/n5_custom_synApps#motor-assignments

=====   ====================================
motor   assignment
=====   ====================================
m23     6-circle diffractometer M_MU
m24     6-circle diffractometer M_OMEGA
m25     6-circle diffractometer M_CHI
m26     6-circle diffractometer M_PHI
m27     6-circle diffractometer M_GAMMA
m28     6-circle diffractometer M_DELTA
m29     4-circle diffractometer M_TTH
m30     4-circle diffractometer M_TH
m31     4-circle diffractometer M_CHI
m32     4-circle diffractometer M_PHI
=====   ====================================

The 4-circle motors are assigned in the ioC.  The 6-circle motors
are chosen here, different from the 4-circle motors.

.. autosummary::

    ~FourCircle
    ~SixCircle
"""

import logging

import hkl
from ophyd import Component
from ophyd import EpicsMotor
from ophyd import EpicsSignalRO
from ophyd import FormattedComponent as FCpt

logger = logging.getLogger(__name__)
logger.bsdev(__file__)


class FourCircle(hkl.SimMixin, hkl.E4CV):
    """
    Our 4-circle.  Eulerian, vertical scattering orientation, with EpicsMotor records.

    Energy obtained (RO) from monochromator.
    """

    # the reciprocal axes are defined by SimMixin

    omega = FCpt(EpicsMotor, "{prefix}{m_th}", kind="hinted", labels=["motor"])
    chi = FCpt(EpicsMotor, "{prefix}{m_chi}", kind="hinted", labels=["motor"])
    phi = FCpt(EpicsMotor, "{prefix}{m_phi}", kind="hinted", labels=["motor"])
    tth = FCpt(EpicsMotor, "{prefix}{m_tth}", kind="hinted", labels=["motor"])

    energy = Component(EpicsSignalRO, "BraggERdbkAO", kind="hinted", labels=["energy"])
    energy_units = Component(EpicsSignalRO, "BraggERdbkAO.EGU", kind="config")

    def __init__(self, prefix, *, m_th="", m_chi="", m_phi="", m_tth="", **kwargs):  # noqa D107
        self.m_th = m_th
        self.m_chi = m_chi
        self.m_phi = m_phi
        self.m_tth = m_tth
        super().__init__(prefix, **kwargs)


class SixCircle(hkl.SimMixin, hkl.E6C):
    """
    Our 6-circle.  Eulerian.

    Energy obtained (RO) from monochromator.
    """

    # the reciprocal axes are defined by SimMixin

    mu = FCpt(EpicsMotor, "{prefix}{m_mu}", kind="hinted", labels=["motor"])
    omega = FCpt(EpicsMotor, "{prefix}{m_omega}", kind="hinted", labels=["motor"])
    chi = FCpt(EpicsMotor, "{prefix}{m_chi}", kind="hinted", labels=["motor"])
    phi = FCpt(EpicsMotor, "{prefix}{m_phi}", kind="hinted", labels=["motor"])
    gamma = FCpt(EpicsMotor, "{prefix}{m_gamma}", kind="hinted", labels=["motor"])
    delta = FCpt(EpicsMotor, "{prefix}{m_delta}", kind="hinted", labels=["motor"])

    energy = Component(EpicsSignalRO, "BraggERdbkAO", kind="hinted", labels=["energy"])
    energy_units = Component(EpicsSignalRO, "BraggERdbkAO.EGU", kind="config")

    def __init__(  # noqa D107
        self,
        prefix,
        *,
        m_mu="",
        m_omega="",
        m_chi="",
        m_phi="",
        m_gamma="",
        m_delta="",
        **kwargs,
    ):
        self.m_mu = m_mu
        self.m_omega = m_omega
        self.m_chi = m_chi
        self.m_phi = m_phi
        self.m_gamma = m_gamma
        self.m_delta = m_delta
        super().__init__(prefix, **kwargs)
