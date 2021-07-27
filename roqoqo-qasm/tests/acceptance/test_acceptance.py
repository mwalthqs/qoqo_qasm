# Copyright © 2019-2021 HQS Quantum Simulations GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
"""Test roqoqo QASM acceptance with qiskit"""
import pytest
from qiskit import QuantumCircuit
from qiskit import sys
import tempfile
import os


def test_acceptance_with_qiskit() -> None:
    """Test gate operations with QASM interface"""
    # import temporary *.qasm file (pre-created by test_aceptance.rs)
    tempdir = tempfile.gettempdir()
    q_circuit = QuantumCircuit.from_qasm_file(tempdir+"/test_simple_rust.qasm")

    assert(q_circuit.depth() > 0)

    # remove temp file generated for and used in this unit test
    os.remove(tempdir+"/test_simple_rust.qasm")


if __name__ == '__main__':
    pytest.main(sys.argv)
