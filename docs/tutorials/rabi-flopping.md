# Single qubit Rabi flopping

First, let's implement a single-qubit Rabi flopping experiment. 
Here, a two-level system, initialized in the $\ket{0}$ basis state, oscillates between $\ket{0}$ and $\ket{1}$ during evolution.
The Hamiltonian under which the state evolves is,
$$
H = -\frac{\pi}{4}\sigma^x
$$

### Building the quantum program

We will go through how to specify this quantum program using OQD's analog interface. First import the relevant modules,
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

Then we construct an [`AnalogGate`][oqd_core.interface.analog.operation.AnalogGate] object,
```py
X = PauliX()
gate = AnalogGate(hamiltonian= -(np.pi / 4) * X)
```

The [`AnalogCircuit`][oqd_core.interface.analog.operation.AnalogCircuit] represents a sequence of Hamiltonians 
which the quantum system evolves under for a fixed duration. Let's construct a circuit and add the gate from above and 
then measure,
```py
circuit = AnalogCircuit()
circuit.evolve(duration=3, gate=gate)
circuit.measure()
```

### Setting up the backend
Now, let's emulate the time dynamics of our quantum system. We use one of the provided backends, 
here the [`QutipBackend`][oqd_analog_emulator.qutip_backend.QutipBackend], to solve the evolution of the quantum state
through the circuit. We first initialize the backend and a [`TaskArgsAnalog`][oqd_core.backend.task.TaskArgsAnalog] 
object with the settings for the emulation, such as the number of shots, 
the metrics to track through the evolution (e.g., an expectation value), and the time step.
```py
backend = QutipBackend()
args = TaskArgsAnalog(
    n_shots=100,
    metrics={
        "Z": Expectation(operator=Z),
    },
    dt=1e-3,
)
```


### Running the backend emulation
Now, we simply use the `.run()` method of the backend to run the emulation of the time dynamics of the circuit.
``` py
results = backend.run(task = task)
```

