
### Bloodstone
* Ion species: <sup>171</sup>Yb<sup>+</sup>
* Target number of qubits: 30 – 50
* Trap architecture: Segmented Blade Trap
* SPAM individual addressing: DMD
* Coherent individual addressing with: Double-pass AOM + AOD

![Bloodstone - Vacuum Chamber & Trap 1](./img/bloodstone-trap1.png){: style="width:300px"}
![Bloodstone - Vacuum Chamber & Trap 2](./img/bloodstone-trap2.png){: style="width:300px"}

### Beryl
* Ion species: <sup>133</sup>Ba<sup>+</sup>, <sup>137</sup>Ba<sup>+</sup>, <sup>138</sup>Ba<sup>+</sup>
* Target number of qubits: 16
* Trap architecture: [Sandia National Laboratories Phoenix Trap (HOA 2.0 platform)](https://arxiv.org/abs/2009.02398)
* SPAM individual addressing: AOMs
* Coherent individual addressing: Laser written waveguide + AOMs

![Beryl - Vacuum Chamber & Trap](./img/beryl-trap.png){: style="width:600px"}

## Real-time Control System
The OQD stack builds on the [Sinara](https://m-labs.hk/experiment-control/sinara-core/) and [ARTIQ](https://m-labs.hk/artiq/) ecosystems for real-time control.

### Sinara
[Sinara](https://sinara-hw.github.io/) is an open-source hardware ecosystem originally designed for use in quantum physics experiments running the ARTIQ control software.
The hardware is also suitable for a broad range of laboratory and test & measurement applications.
It is licensed under CERN OHL v1.2.


### ARTIQ (Advanced Real-Time Infrastructure for Quantum)
[The Advanced Real-Time Infrastructure for Quantum physics framework](https://github.com/m-labs/artiq) is a software framework developed by M-Labs that provides Python bindings to the Sinara real-time signal generation and detection apparatus at the core of the electrical apparatus.
ARTIQ functions by exposing control of the individual channels of custom-specified Sinara hardware in the Python programming language.
The system maintains an internal clock and timeline.
Events specified programmatically by the user are applied to the timeline and sent to the Sinara hardware with a series of queues.
The Sinara hardware then executes the instructions with nanosecond precision on a series of FPGAs.

### DAX (Duke ARTIQ Extensions)
[The Duke ARTIQ Extensions (DAX)](https://gitlab.com/duke-artiq/dax) are additional tools and capabilities drawn from traditional software design principles for the ARTIQ framework.
ARTIQ allows low-level access to individual channels on the Sinara hardware.
DAX provides a framework for grouping channels into logical modules representing appropriate experimental apparatus abstractions and services that use those modules to perform regular, repeatable tasks.
