# Transverse field Ising model 

Next, let's implement everyone's favourite many-body Hamiltonian -- the transverse-field Ising model.
The Hamiltonian is of the form,

$$
H = \sum_{\langle ij \rangle} \sigma^x_i \sigma^x_j + h \sum_i \sigma^z_i
$$

We will first implement this for two qubits only, and then expand to a larger system size.
Throughout, we will use a transverse field strength of $h=1$,

$$
H = \sigma^x_1 \sigma^x_2 + \sigma^z_1 + \sigma^z_2
$$

### Building the quantum program

First we import the relevant modules,
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

As before, we can describe the Hamiltonian using the operators in the analog layer interface.
```py
X, Z, I = PauliX(), PauliZ(), PauliI()

hamiltonian = (X @ X) + (Z @ I) + (I @ Z)
gate = AnalogGate(hamiltonian=hamiltonian)

circuit = AnalogCircuit()
circuit.evolve(duration=5, gate=gate)
circuit.measure()
```

To generalize this to `n` qubits, we can use built-in Python operations and libraries,
```py
import functools
from operator import matmul, add

X, Z, I = PauliX(), PauliZ(), PauliI()

n = 5

hamiltonian_xx = functools.reduce(
    add, [functools.reduce(matmul, [X if i in (j, (j+1)%n) else I for i in range(n)]) for j in range(n)]
)
hamiltonian_z = functools.reduce(
    add, [functools.reduce(matmul, [Z if i==j else I for i in range(n)]) for j in range(n)]
)
gate = AnalogGate(hamiltonian=hamiltonian_xx + hamiltonian_z)

circuit = AnalogCircuit()
circuit.evolve(duration=5, gate=gate)
circuit.measure()
```


### Setting up and running the classical emulation
Similarly, we set up the settings for the classical emulation backend, 
including the number of shots and metrics (e.g., expectation values, entropy of entanglement) 
which we want to track through the time evolution.

```py
args = TaskArgsAnalog(
    n_shots=100,
    metrics={
        'entanglement_entropy': EntanglementEntropyVN(qreg = [1]),
    },
    dt=1e-2,
)

backend = QutipBackend()
results = backend.run(task = task)
```