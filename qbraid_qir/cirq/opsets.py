# Copyright (C) 2023 qBraid
#
# This file is part of the qBraid-SDK
#
# The qBraid-SDK is free software released under the GNU General Public License v3
# or later. You can redistribute and/or modify it under the terms of the GPL v3.
# See the LICENSE file in the project root or <https://www.gnu.org/licenses/gpl-3.0.html>.
#
# THERE IS NO WARRANTY for the qBraid-SDK, as per Section 15 of the GPL v3.

"""
Module defining supported Cirq operations/gates.

"""
import cirq
import pyqir._native

# "barrier",
# "mz",
# "reset",
# "s_adj",
# "t_adj",
CIRQ_GATES = {
    'TOFFOLI': pyqir._native.ccx,
    'CCX': pyqir._native.ccx,
    'CCNOT': pyqir._native.ccx,
    'CNOT': pyqir._native.cx,
    'CZ': pyqir._native.cz,
    'H': pyqir._native.h,
    'S': pyqir._native.s,
    'SWAP': pyqir._native.swap,
    'T': pyqir._native.t,
    'X': pyqir._native.x,
    'Y': pyqir._native.y,
    'Z': pyqir._native.z,
    }

def get_callable_from_pyqir_name(op: cirq.Operation):
    """Get callable from pyqir name."""
    return CIRQ_GATES[str(op.gate)]

# some testcases for the above function
circuit = cirq.Circuit()
circuit.append(cirq.ops.CNOT(cirq.LineQubit(0), cirq.LineQubit(1)))
circuit.append(cirq.ops.CNOT(cirq.LineQubit(1), cirq.LineQubit(2)))
circuit.append(cirq.ops.CNOT(cirq.LineQubit(2), cirq.LineQubit(3)))
circuit.append(cirq.ops.H(cirq.LineQubit(0)))
circuit.append(cirq.ops.H(cirq.LineQubit(1)))

for op in circuit.all_operations():
    print(get_callable_from_pyqir_name(op))
