#%% md
# One qubit Rabi flopping

#%%
import numpy as np
from rich import print as pprint
import matplotlib.pyplot as plt
import seaborn as sns

#%%
from midstack.interface.analog.operator import *
from midstack.interface.analog.operation import *
from midstack.backend.metric import *
from midstack.backend.task import Task, TaskArgsAnalog

from analog_sim.base import QutipBackend

from client import Client
from provider import Provider

#%%
X = PauliX()
Z = PauliZ()

Z.model_validate_json(Z.model_dump_json())

Hx = AnalogGate(hamiltonian=(2*X+Z))

#%%
op = (2*X+Z)
print(op.model_dump_json())


#%%
print(Hx)
print(Hx.model_dump_json())
print(AnalogGate.model_validate_json(Hx.model_dump_json()))

#%%
circuit = AnalogCircuit()
circuit.evolve(duration=10, gate=Hx)

print(circuit)
print(circuit.model_dump_json())
print(AnalogCircuit.model_validate_json(circuit.model_dump_json()))

#%%
# define task args
args = TaskArgsAnalog(
    n_shots=100,
    fock_cutoff=4,
    metrics={
        "Z": Expectation(operator=Z),
    },
    dt=1e-3,
)

task = Task(program=circuit, args=args)

#%%
backend = QutipBackend()
expt, args = backend.compile(task=task)
results = backend.run(experiment=expt, args=args)

#%%
fig, ax = plt.subplots(1, 1, figsize=[6, 3])
colors = sns.color_palette(palette="crest", n_colors=4)

for k, (name, metric) in enumerate(results.metrics.items()):
    ax.plot(results.times, metric, label=f"$\\langle {name} \\rangle$", color=colors[k])
ax.legend()
plt.show()

#%%
fig, axs = plt.subplots(4, 1, sharex=True, figsize=[5, 9])

state = np.array([basis.real + 1j * basis.imag for basis in results.state])
bases = ["0", "1"]
counts = {basis: results.counts.get(basis, 0) for basis in bases}

ax = axs[0]
ax.bar(x=bases, height=np.abs(state) ** 2, color=colors[0])
ax.set(ylabel="Probability")


ax = axs[1]
ax.bar(x=bases, height=list(counts.values()), color=colors[1])
ax.set(ylabel="Count")


ax = axs[2]
ax.bar(x=bases, height=state.real, color=colors[2])
ax.set(ylabel="Amplitude (real)")

ax = axs[3]
ax.bar(x=bases, height=state.imag, color=colors[3])
ax.set(xlabel="Basis state", ylabel="Amplitude (imag)", ylim=[-np.pi, np.pi])

plt.show()

#%%
client = Client()
provider = Provider()
client.connect(
    provider=provider,
    username="benjimaclellan",
    password="pwd"
)
client.status_report

#%%
# print(client.jobs)
backend = "qutip"
client.submit_job(task=task, backend="qutip")

#%%
provider.job_submission_url(backend=backend)


#%%
t = task.model_dump_json()
AnalogCircuit.parse_raw(circuit.model_dump_json())


#%%