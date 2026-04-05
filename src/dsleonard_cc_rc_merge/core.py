#!/bin/env python3
# main.py
# Copyright  Douglas Leonard 2026.
#
# License: MIT, attribution required
#
# provided skeleton by D.S. Leonard, MIT licensed.

#Setup useful verbosity controls for messaging and shell command execution via qx:
#see https://github.com/DSLeonard-coding/qx
from dsleonard_qx import *  # noqa so linters won't move this # type: ignore

#The core file gets names in __all__ exported to top level for
# from package.module import *
#Other modules just get the module name exported
__all__=[
    'dsleonard_cc_rc_merge',
]

#From bash, use export dsleonard_cc_rc_merge_DEBUG="True" to enable debug output
_DEBUG: bool = False   # print commands called with qx commands
if "dsleonard_cc_rc_merge_DEBUG" in os.environ:
    _DEBUG = True
_PRETEND: bool = False  #Option to only print qx commands, not run.

def setup_qx():
    qx.verbosity_thresholds(qx.INFO)
    if _DEBUG or _PRETEND:
        qx.verbosity_thresholds(qx.DEBUG)   # Debug output level
    # Edit default output severity for qx command echoing and stdout, and set pretend
    qx.defaults(out_lvl=qx.INFO, echo_lvl=qx.INFO, pretend=_PRETEND)

#Main entry point for project.
#Edit project.scripts in pyproject.toml if you rename it, or to change the cli name
def dsleonard_cc_rc_merge():
    setup_qx()
    msg("This is dsleonard_cc_rc_merge")  #qx.INFO level message
    msg("Edit this code in src/dsleonard_cc_rc_merge/main.py")  #qx.INFO level message
    qx('echo "Hello World!"')  # a simple shell command.
    dbg("This method only displays with _DEBUG == True")
