"""Device factories."""

from apstools.utils import dynamic_import

# class EpicsMotor_SREV(EpicsMotor):
#     """Provide access to motor steps/revolution configuration."""
#
#     steps_per_revolution = Component(EpicsSignal, ".SREV", kind="config")


def motors(
    prefix=None,
    names="m{}",
    first=0,
    last=0,
    class_name="ophyd.EpicsMotor",
    **kwargs,
):
    """
    Make one or more ``ophyd.EpicsMotor`` objects.

    Example entry in `devices.yml` file:

    .. code-block:: yaml
        :linenos:

        instrument.devices.factories.motors:
          - {prefix: "ioc:m", first: 1, last: 4, labels: ["motor"]}
          # skip m5 & m6
          - {prefix: "ioc:m", first: 7, last: 22, labels: ["motor"]}

    Uses this pattern:

    .. code-block:: py
        :linenos:

        ophyd.EpicsMotor(
                prefix=prefix.format(i),
                name=names.format(i),
                **kwargs,
            )

    where ``i`` iterates from 'first' through 'last' (inclusive).

    PARAMETERS

    prefix : str
        Name *pattern* for the EPICS PVs.  There is no default pattern. If a
        formatting specification (``{}``) is not  provided, it is appended (as
        with other ophyd devices).  Each motor will be configured with this
        prefix: ``prefix.format(number)``, such as::

            In [23]: "ioc:m{}".format(22)
            Out[23]: 'ioc:m22'

    names : str
        Name *pattern* for the motors.  The default pattern is ``"m{}"`` which
        produces motors named ``m1, m2, ..., m22, m23, ...```.  If a formatting
        specification (``{}``) is not provided, it is appended.  Each motor
        will be named using this code: ``names.format(number)``, such as::

            In [23]: "m{}".format(22)
            Out[23]: 'm22'

    first : int
        The first motor number in the continuous series from 'first' through
        'last' (inclusive).

    last : int
        The first motor number in the continuous series from 'first' through
        'last' (inclusive).

    kwargs : dict
        Dictionary of additional keyword arguments.  This is included
        with each EpicsMotor object.
    """
    if "{" not in names:
        names += "{}"
    if prefix is None:
        raise ValueError("Must define a string value for 'prefix'.")
    if "{" not in prefix:
        prefix += "{}"

    klass = dynamic_import(class_name)

    first, last = sorted([first, last])
    for i in range(first, 1 + last):
        yield klass(prefix=prefix.format(i), name=names.format(i), **kwargs)
