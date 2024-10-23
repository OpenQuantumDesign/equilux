# Transverse field Ising model (TFIM)

Let's implement our favourite Hamiltonian -- the transverse-field Ising model.
The general Hamiltonian looks like,

$$
H = \sum_{\langle ij \rangle} \sigma^x_i \sigma^x_j + h \sum_i \sigma^z_i
$$

Let's implement it with two qubits and with $h=1$.

$$
H = \sigma^x_1 \sigma^x_2 + \sigma^z_1 + \sigma^z_2
$$

## Implementation

We will go through this step by step. First we get the necessary imports:
/// details | Imports

```py
import numpy as np

from oqd_core.interface.analog.operator import PauliI, PauliX, PauliZ, PauliY
from oqd_core.interface.analog.operation import *
from oqd_core.backend.metric import *
from oqd_core.backend.task import Task
from oqd_analog_emulator.qutip_backend import QutipBackend
```

///

Then we build a [`AnalogGate`][oqd_core.interface.analog.operations.AnalogGate] object:

```py
"""For simplicity we initialize some Operators"""
X, Z, I = PauliX(), PauliZ(), PauliI()

gate = AnalogGate(
    hamiltonian= (X @ X) + (Z @ I) + (I @ Z),
)
```

Then we define the [`AnalogCircuit`][oqd_core.interface.analog.operations.AnalogCircuit] object and evolve it according to the hamiltonian defined above

```py
circuit = AnalogCircuit()
circuit.evolve(duration=5, gate=gate)
```

For analog emulation, we first define the arguments to pass to the classical emulation, 
including the number of shots and metrics (e.g., expectation values, entropy of entanglement) which we want to track 
through the time evolution.

```py
args = TaskArgsAnalog(
    n_shots=100,
    fock_cutoff=4,
    metrics={
        'entanglement_entropy': EntanglementEntropyVN(qreg = [1]),
    },
    dt=1e-2,
)
```

We then wrap the [`AnalogCircuit`][oqd_core.interface.analog.operations.AnalogCircuit] and the arguments to a [`Task`][oqd_core.backend.task.Task] object and run using the QuTip backend. 

## Running the simulation

First initialize the [`QutipBackend`][oqd_analog_emulator.qutip_backend.QutipBackend] object.
=== "Compile & Simulate"
The [`Task`][oqd_core.backend.task.Task] is compiled to a [`QutipExperiment`][oqd_analog_emulator.qutip_backend.QutipExperiment] 
object and then this [`QutipExperiment`][oqd_core.backend.qutip.interface.QutipExperiment], composed of `qt.QObj` objects. 
This is to allow you to see what parameters are used to specify the particular QuTip experiment.

``` py
backend = QutipBackend()
results = backend.run(task = task)
```