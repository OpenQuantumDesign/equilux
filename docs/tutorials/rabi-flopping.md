# Single qubit Rabi flopping

Let's implement the single qubit Rabi Flopping,

$$
H = -\frac{\pi}{4}\sigma^x
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

Then we define the [`AnalogGate`][oqd_core.interface.analog.operations.AnalogGate] object

```py
"""For simplicity, we initialize the X Operator"""
X = PauliX()

gate = AnalogGate(hamiltonian= -(np.pi / 4) * X)
```

Then we define the [`AnalogCircuit`][oqd_core.interface.analog.operations.AnalogCircuit] object and evolve it according to the Hamiltonian defined above

```py
ac = AnalogCircuit()
ac.evolve(duration=3, gate=gate)
```

For QuTip simulation we need to define the arguements which contain the number of shots and the metrics we want to evaluate.

```py
args = TaskArgsAnalog(
    n_shots=100,
    fock_cutoff=4,
    metrics={
        "Z": Expectation(operator=Z),
    },
    dt=1e-3,
)
```


## Running the simulation

First initialize the [`QutipBackend`][oqd_analog_emulator.qutip_backend.QutipBackend] object.


``` py
backend = QutipBackend()
results = backend.run(task = task)
```