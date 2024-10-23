# ![Open Quantum Design](./img/oqd-logo-text.png)

<div align="center">
    <h2 align="center">
        Program the world's first open-source, full-stack quantum computer.
    </h2>
</div>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
[![GitHub Workflow Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/ki3-qbt/graph-compiler/actions)

<!-- prettier-ignore -->
/// admonition | Note
    type: note
Welcome to the Open Quantum Design framework for programming quantum computers.
This documentation is still under development, please feel to contribute! © Open Quantum Design
///

## What's here
Open Quantum Design is a non-profit foundation to build full-stack, open-source quantum computing designs.
This documentation includes the software components of the OQD stack, including the core programming interfaces,
classical emulation backends, compiler infrastructure, and cloud server containers.

## The stack
OQD's quantum computer stack can be interfaced at different levels, including the digital layer, analog layer, and atomic layer.
![](figures/stack_diagram.png)

## Getting Started <a name="Getting Started"></a>
Here's a short example of how to use the analog interface to specify, serialize, and simulate an analog quantum program. 
We use a simple, single-qubit Rabi-flopping experiment as an example:
```python
from oqd_core.interface.analog.operator import PauliZ, PauliX
from oqd_core.interface.analog.operation import AnalogCircuit, AnalogGate
from oqd_core.backend.metric import Expectation
from oqd_core.backend.task import Task, TaskArgsAnalog
from oqd_analog_emulator.qutip_backend import QutipBackend

X = PauliX()
Z = PauliZ()

Hx = AnalogGate(hamiltonian=X)

circuit = AnalogCircuit()
circuit.evolve(duration=10, gate=Hx)
circuit.measure()

args = TaskArgsAnalog(
  n_shots=100,
  fock_cutoff=4,
  metrics={"Z": Expectation(operator=Z)},
  dt=1e-3,
)

task = Task(program=circuit, args=args)

backend = QutipBackend()
results = backend.run(task=task)
```
